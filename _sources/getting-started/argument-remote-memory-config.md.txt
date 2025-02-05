# Argument ${REMOTE_MEMORY_CONFIG}

:::{code-block} console
--remote-memory-configuration: path to the memory configuration file
:::

## Analytical Remote Memory Config

Example remote memory configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/examples/network_analytical/remote_memory.json
:::

- **memory-type**: (string) memory type ("NO_MEMORY_EXPANSION", "PER_NODE_MEMORY_EXPANSION", "PER_NPU_MEMORY_EXPANSION", or "MEMORY_POOL")

- **remote-mem-latency**: (uint) remote memory latency (ns)

- **remote-mem-bw**: (uint) remote memory bandwidth (GB/s or B/ns)

- **num-nodes**: (int) number of nodes (only valid with "PER_NODE_MEMORY_EXPANSION")

- **num-npus-per-node**: (int) number of NPUs per node (only valid with "PER_NODE_MEMORY_EXPANSION")
