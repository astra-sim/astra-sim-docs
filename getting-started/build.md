# Build ASTRA-sim

:::{note}
Please make sure that you have all the required depencencies installed.
:::

## Clone Repository

:::{code-block} console
git clone --recurse-submodules git@github.com:astra-sim/astra-sim.git
ASTRA_SIM=$(realpath ./astra-sim)
:::

## Compile Program

:::{code-block} console
cd ${ASTRA_SIM}
::: 

### Analytical Network Backend
:::{code-block} console
./build/astra_analytical/build.sh
:::

Once built, the executable `${ASTRA_SIM_BIN}` is located at:

:::{code-block} console
ASTRA_SIM_BIN=${ASTRA_SIM}/build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Aware
:::

### NS3 Network Backend
:::{code-block} console
./build/astra_ns3/build.sh -c
:::




