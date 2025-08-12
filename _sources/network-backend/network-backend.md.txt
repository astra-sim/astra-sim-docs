# Network Backend

:::{note}
This page is currently under construction. Please stay tuned for updates!
:::

ASTRA-sim currently supports three network simulators as its communication modeling backend.
- Analytical Network Simulator [Source Code Directory](https://github.com/astra-sim/astra-sim/tree/master/astra-sim/network_frontend/analytical)
- ns-3 Network Simulator [Source Code Directory](https://github.com/astra-sim/astra-sim/tree/master/astra-sim/network_frontend/ns3)
- Garnet (from gem5) Network Simulator

Users can also define their own custom network backend.

:::{toctree}
analytical-network-backend.md
ns3-network-backend.md
garnet-network-backend.md
custom-network-backend.md
:::
