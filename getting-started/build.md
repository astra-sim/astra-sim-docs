# Build ASTRA-sim

:::{note}
Please make sure that you have all the required dependencies or Docker installed. If not, please refer to the [Setup ASTRA-Sim](./setup.md).
:::
## Compile Program

### Analytical Network Backend
:::{code-block} console
./build/astra_analytical/build.sh
:::

This builds two variants:
- **Congestion-aware:** `AstraSim_Analytical_Congestion_Aware` — models network congestion effects
- **Congestion-unaware:** `AstraSim_Analytical_Congestion_Unaware` — simpler, faster simulation

The executables are located at:

:::{code-block} console
${ASTRA_SIM}/build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Aware
${ASTRA_SIM}/build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Unaware
:::

### NS-3 Network Backend
:::{code-block} console
./build/astra_ns3/build.sh -c
:::

Compile and run with `./build/astra_ns3/build.sh -r`.




