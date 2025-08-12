# Build ASTRA-sim

:::{note}
Please make sure that you have all the required depencencies or docker installed. If not, please refer to the [Setup ASTRA-Sim](./setup.md) 
:::
## Compile Program

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




