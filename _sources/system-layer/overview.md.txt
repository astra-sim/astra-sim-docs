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
:::{note}
This section is currently under construction. Please stay tuned for updates!
:::

## Interface with network backend
:::{note}
This section is currently under construction. Please stay tuned for updates!
:::