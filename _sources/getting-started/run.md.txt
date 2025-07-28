# Run ASTRA-sim

Run simulations by passing the required aruguments:

:::{code-block} console
${ASTRA_SIM_BIN} \
  --workload-configuration=${WORKLOAD_CONFIG} \
  --system-configuration=${SYSTEM_CONFIG} \
  --network-configuration=${NETWORK_CONFIG} \
  --remote-memory-configuration=${REMOTE_MEMORY_CONFIG} \
  --comm-group-configuration=${COMM_GROUP_CONFIG}
:::

:::{toctree}
argument-workload-config.md
argument-system-config.md
argument-network-config.md
argument-remote-memory-config.md
argument-comm-group-config.md
:::

:::{note}
Additional arguments may be required based on the type of network backend.
:::