# Connecting a Custom Network Backend

## Overview
ASTRA-sim's strength lies in its modularity, where users can easily switch between different backends in a plug-and-play manner. Here, we provide a description of how users can add their own network backend, instead of choosing from the Analytical or ns-3 backend that ASTRA-sim currently supports. Adding a new network backend is as easy as implementing the network API (source) and initializing the simulator (writing the main function). Users can refer to the following examples when going through this documentation. 

- Analytical Network Simulator: astra-sim/network_frontend/analytical
- ns-3 Network Simulator: astra-sim/network_frontend/ns3

## Conceptual Recap
In ASTRA-sim, the network backend should manage the simulated clock(timeline). 
The System layer breaks down a collective operation into send and receive messages (i.e. the source and destination is already determined) and commands the network backend to simulate these messages. It is upto the network backend to simulate the network event and forward the simulated clock (for example, by registering a 'send complete' event in a future timestamp).
When the simulator sees a non-communication operator, such as a compute operator, it will simulate the operation with the respective backend and obtain the simulated duration. The simulator will tell the network backend to advance the simulated clock by the simulated duration. 

The Network API is the interface between the System layer and the network backend. Through this API the system, representing the reset of the simulator, commands the network backend to simulate message events or forward the simulated clock. The user has to implement a 'network handler', which implements this Netowrk API and issues necessary commands to the actual simulator.
Note that ASTRA-sim is an event based discrete simulator. This allows the control flow to pass between the network backend and the rest of the simulator (While the control flow is within the rest of the simulator, such as the System layer or the compute backend, the simulated clock is 'paused', and no event is 'taking place simultaneously'). 

The system layer consists of multiple instances of the `Sys` class, where one instance corresponds to one process (rank). When constructing the `Sys` class instance, the user needs to provide it with a handler of the network backend that implements the Network API. For this reason, in ASTRA-sim, the main function (i.e. constructing the `Sys` class) is unique to each network backend and must be implemented uniquely to the network backend. 


## Detailed Implementaiton 
### Network API
We now discuss implementing the network API in detail. The network API definition can be found [here]
(https://github.com/astra-sim/astra-sim/blob/master/astra-sim/system/AstraNetworkAPI.hh)

:::{note}
The description below will be migrated as comments to the actual AstraNetworkAPI.hh file. 
::: 

Similar to the `Sys` class, when defining a network handler class implementing the network API, there should be one instance per process (rank).

- `sim_send`: The system layer tells the network handler to simulate a network message from the handler class' internal rank to `dst`. The system layer also provides a callback function through the `msg_handler` argument. 
The network handler should return the `sim_send` function immediately after registering this callback function, and NOT wait until the message send 'has completed'. Once the network simulator simulates that the message has left the source rank, the handler should call the callback function, passing the control back to the system layer.  
 
- `sim_recv`: The system layer tells the network handler to *expect* a message from `src` to the handler class' internal rank. The system layer also provides a callback function through the `msg_handler` argument.
Similar to `sim_send`, the network simulator should return immediately after registering this callback function. 
When the message actually (is simiulated to have been) received, the network handler should call the callback function, passing the control flow back to the system layer. 

- `sim_schedule`: `sim_schedule` is used when ASTRA-sim wants to schedule an event on the network backend. The function arguments define the duration of the simulated event. Once the registration is completed, the handler should return immediately. Once the event, scheduled `delta` time later, is triggered, call the callback function in `fun_arg`. 

- `sim_get_time`: Get the *simulated* time.



### Main function
Now that we implemented the network handler class, we need to write the main function that initializes everything. For this, we will refer to the ns3 backend's main function as an example. Here the `ASTRASimNetwork` class is the ns-3 simulator specific network handler that we defined. This handler class implements the network API as defined above. (The implementation is detailed in the [entry.h](https://github.com/astra-sim/astra-sim/blob/ccb194879c2fab9f3ed873ab4e33f45c7aeec805/astra-sim/network_frontend/ns3/entry.h) file). The rest of the file is as follows: 

1. Read and parse the input files: link
The configuration files for the Workload, System, Memory, and Communicator group is the same across all network backends. The simulator expects the path to these configuration files. Write argument flags that accepts these flags. While it is free for the user to use whichever flag name, for the sake of continuity we suggest users to use existing flags, such as  `--system-configuration`, `--workload-configuration`, etc. On the other hand, the user has full control on what format to use for the configuration for the network simulator.  

2. Instantiate the network handler and the `Sys` class. 
For each rank, instantiate one instance of the network handler, and the `Sys` class. Note how we provide the reference to the network handler to the `Sys` class. Also provide the configuration paths that we have parsed in the above stage. 

3. Initialize the network simulator. 
Parse the network configuration file, and set up the topology, , etc. as necessary. 

4. Start issuing operators from the workload. 
The `fire()` function tells the workload layer to start iterating through the Chakra ET, and issue operators without any dependencies. Communication operators will register (but not start) message sends/receives through the `sim_send/receive` API calls, while other operators such as compute operators will simulate the compute duration and register a 'compute end' event through `sim_schedule`. Once the workload layer iterates through the Chakra ET and determines there are no more operations it can issue, it returns the `fire()` function. 

5. Start the simulated timeline in the network simulator. 
We now start the network simulator to go through the simulated timeline and trigger events registered by step 4. When an event (receive has completed, etc.) it will call the callback function passed in the function. This passes the control flow to the system layer, and then the workload layer, which will issue new nodes whose dependencies have been resolved. Once there are no more Chakra nodes to issue, the network simulator should forward the simulated timeline, and issue the next set of events in the next available timestamp



