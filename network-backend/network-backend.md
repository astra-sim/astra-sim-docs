# Network Backend

:::{note}
This page is currently under construction. Please stay tuned for updates!
:::

ASTRA-sim supports multiple network simulators as its communication modeling backend:

- **Analytical Network Simulator** [Source Code Directory](https://github.com/astra-sim/astra-sim/tree/master/astra-sim/network_frontend/analytical) — models communications through analytical equations, suitable for large-scale simulations
- **ns-3 Network Simulator** [Source Code Directory](https://github.com/astra-sim/astra-sim/tree/master/astra-sim/network_frontend/ns3) — packet-level discrete event simulation with realistic network modeling
- **HTSim Network Simulator** — cycle-accurate network simulation (Broadcom CSIM-HTSim)

:::{warning}
**Garnet (from gem5)** — This backend is no longer actively maintained.
:::

Users can also define their own custom network backend.

:::{toctree}
analytical-network-backend.md
ns3-network-backend.md
garnet-network-backend.md
custom-network-backend.md
:::
