# System Layer

The Workload layer iterates over the nodes in the Chakra ET and issues commands for the operation each Chakra ET node refers to. The system layer takes these commands and translates them so that the respective Network, Compute, or Memory backends can properly simulate the operation. Depending on the operation, the system layer's behavior changes as follows: 

- Compute operation: Issues a call to the Compute backend to simulate the duration of the operation. 
- Memory operation: Issues a call to the Memory backend to simulate the duration of the operation. 
- Collective operation: Breaks the collective communication into point-to-point send and receive messages, and issues a 'send' or 'receive' call to the network backend to simulate the messages. 

Since the compute and memory operations are fairly straightforward, we focus on how the collective operations are scheduled and executed. [Source Code Directory](https://github.com/astra-sim/astra-sim/tree/master/astra-sim/system)

:::{toctree}
collective-scheduler.md
collective-implementation.md
sysinput.md
:::
