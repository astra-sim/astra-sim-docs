# Overview

## Foreword
This page describes the basic mechanism of the System layer at a very high level. Some details are omitted and/or simplified for clear delivery. Please refer to the codebase and email the user mailing list [astrasim-users@googlegroups.com](mailto:astrasim-users@googlegroups.com) if anything remains unclear.


## Queue Management
![System Layer Queue](/_static/images/system_overview_queue.svg)

Core to the System layer is a set of queues called `active_Streams`.

Each queue holds `StreamBaseline` objects, which are depicted at the top right corner of the image. A `StreamBaseline` object represents a stream (i.e. collective), which consists of multiple collective phases. The variable `phases_to_go` is a queue holding these phases. The pointer `my_current_phase` points to the phase currently being executed.

For each stream, the function `proceed_to_next_vnet_baseline` is critical in advancing the collective phases and moving the stream object between one queue to another.
This function is called in the following possible cases:

1. When a stream has been removed from `ready_list` and is about to be inserted into `active_Streams` for the first time.
2. When a stream has finished one phase and is ready to wait for the next phase.
3. When a stream has finished its last phase.

Let's first look at the behavior of `proceed_to_next_vnet_baseline` at case #2. In the image above, refer to the pink circles (2-1), (2-2), ... (2-5).

1. Look at the queue currently holding the stream. `erase()` the `StreamBaseline` object from the queue, which is really a `list` object. (Note that streams may not finish in the order they start executing.)
2. Modify the StreamBaseline object. The finished collective phase is popped from `phases_to_go`, and `my_current_phase` now points to the next phase to be executed.
3. Insert the `StreamBaseline` object into the next queue using `insert_stream`.
4. Call the function `notify_stream_removed`. This looks at the head of the previous queue. The variable `stream_pointer` points to the frontmost stream which is not running (marked blue). The function starts the execution of this stream's next phase by calling `StreamBaseline::init()`.
5. Similarly, use `notify_stream_added` to trigger the phase of the stream at the head of the new queue.

In the other cases, `proceed_to_next_vnet_baseline` executes a subset of the above steps. In case #1 (stream has just been removed from `ready_list`), `proceed_to_next..` initializes the stream (1-2), inserts it into the first queue (1-3), and triggers the streams at the head of this queue. At case #3 (stream has finished), the function erases the stream from the previous queue (3-1), and triggers the streams at the head of the previous queue. Additionally, the `StreamBaseline` object is `delete`d, and `notify_stream_finished` is called to notify the `Sys` object that a stream has ended (3-6).


## Collective Implementation
The collective implementations of Astra-sim follows general implementations, such as NCCL, but differ slightly in detail.

### Ring
<!-- ![Ring Algorithm](/_static/images/system_collective_ring.svg) -->
In a ring with n nodes, a collective originally in node k will have to go through n-1 communications to traverse through all nodes and arrive at node k-1. From node k's point of view, node k will send n-1 messages and receive n-1 messages.

Here is a detail of how it happens.

1. Node k generates some data within itself. It sends it to node k+1.
2. Node k will receive some data from k-1. After performing some reduce operations (if necessary), it will send this chunk to node k+1.
3. Node k will repeat step 2 for n-2 times.
4. Finally, node k will receive the last data from node k-1. It will not forward this to node k+1. Instead, the Ring communication finishes.

In total, Node k receives messages n-1 times and sends messages n+1 times.


:::{note}
Instead of `n-1`, the number of communications for a Ring implementation of AllReduce is `2n - 1`, and AllToAll is `n*(n-1)`
:::

:::{note}
Other collectives will be updated shortly.
:::

## Interface with network backend
![Collective Iteration](/_static/images/system_collective_iteration.svg)

This section discusses how collectives are triggered by the system layer, and how they issue and receive communications through the network layer. Refer to the above sections for a brief overview on how the `StreamBaseline` object is constructed and executed. Here, we use the `Ring` algorithm as an example to illustrate. The key principles mentioned here apply to the other algorithms.

:::{note}
The numbers marked like `(1)` in the text below correspond to the circles in the image above
:::

### Initialization of collective phase
The `Ring` object is first constructed when the workload layer constructs the `StreamBaseline` object. The following parameters are some of the parameters set during construction.
- `stream_count`: Number of communications needed to complete the Ring communication(The `n-1` number above).
- `curr_sender`: Which node this node should send messages to
- `curr_receiver`: Which node this node should receive messages from

When the StreamBaseline object enters the `running_streams` list, `StreamBaseline::init` starts the collective algorithm by calling `Ring::init`. This function will load the initial data from the NPU into the host memory, through the `send_from_NPU_to_MA` function. The function will register `PacketBundle::call()` as the callback handler which will be triggered once the data is finished loading into memory`(1)`. The duration of loading the data into Memory is simulated by the Memory components.

### Message sending.
When the packets arrive in host memory, `PacketBundle::call()` is triggered, which calls `Ring::ready()``(2)`. Now, we are ready to send the first message to the next node.

First, the node calls `sim_send` to send the message to `curr_sender``(3)`. The network layer implementation of `sim_send` issues a non-blocking command to simulate the message going from this node to `curr_sender`. Right after, `sim_recv` is called. `sim_recv` simply registers `Sys::eventHandler()` as the handler to be triggered when this node receives a message from `curr_receiver`.

Note that both `sim_send` and `sim_recv` are not blocking. There is no strict ordering between a node receiving a message from the previous node, and finishing sending a message to the next node. `sim_recv` simply registers a handler to be called once a message arrives. If the network layer simulates that it received a message `sim_recv` was called, the handler will be triggered immediately.

Once the network layer simulates an incoming message, the handler will eventually call `PacketBundle::call()`, which will read the data from the memory into the NPU`(4)`. Once this is complete, it will call `Ring::ready()` so that this node can forward the message to `curr_sender`. This process is repeated multiple times. (In cases such as AllReduce where a reduce computation needs to happen, such event is also simulated.)

### Terminating ring communication.
`iteratable` is the function that checks whether the Ring communication can finish. It will check two conditions: There are no more messages to send, and the node has received the last message. This is achieved by `iteratable` checking if `stream_count` is 0 after being called by the handler of `sim_recv`.

When the handler registered by `sim_recv` is called, `Ring::run()` is called with `EventType::PacketReceived`. This will eventually call `Ring::run()`, which will call `Ring::ready()`. However, because all of the messages have been sent (`stream_count` is 0), this funciton will return without doing anything significant`(5-1)`. This allows `Ring::iteratable()` to confirm that the collective can finish.

Note that `iteratable` will not exit the communication right after `sim_send` and `sim_recv` is called for the last time`(5-2)`. This is because a separate variable, `free_packets`, tracks if `Ring::ready()` did anything (i.e. `sim_send`, `sim_recv`). Only when `Ring::ready()` does not do anything will `iteratable` end the collective. (i.e. only triggered because `Ring::run` has been called for the last time with `EventType::PacketReceived`)

Once `iteratable` determines this collective has finished, it will call `proceed_next_vnet()`, which will finish this collective communication phase and move the corresponding `StreamBaseline` object.
