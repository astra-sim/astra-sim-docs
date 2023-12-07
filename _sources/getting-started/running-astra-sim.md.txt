# Run ASTRA-sim

Once ASTRA-sim is built, the executable `${BINARY}` is located at:

:::{code-block} console
# For the analytical network backend
$ ${ASTRA_SIM}/build/astra_analytical/build/AnalyticalAstra/bin/AnalyticalAstra
:::

Run simulations by passing the required aruguments:

:::{code-block} console
$ ${BINARY} \
  --workload-configuration=${WORKLOAD_CONFIG} \
  --system-configuration=${SYSTEM_CONFIG} \
  --network-configuration=${NETWORK_CONFIG} \
  --remote-memory-configuration=${MEMORY_CONFIG}
:::

:::{toctree}
argument-workload-config.md
argument-system-config.md
argument-network-config.md
argument-memory-config.md
:::

:::{note}
Additional arguments may be required based on the type of network backend.
:::
