# Argument ${NETWORK_CONFIG}

:::{code-block} console
--network-configuration: path to the network configuration file
:::

## [Analytical Network Config](https://github.com/astra-sim/astra-network-analytical/tree/40d3d0ff11bfd241b20423f1d9b5c670dc0d5bd8)

Example network configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/inputs/network/analytical/
:::

- **topology-name**: (string) put "Hierarchical"

- **dimensions-count**: (uint) number of network dimensions

:::{note}
Each configurations below is represented as an array of size **dimensions-count**, indexed by the dimension level.
:::

- **topologies-per-dim**: (string) network topology ("Ring", "FullyConnected", or "Switch")

- **dimension-type**: (string) dimension type ("Tile", "Package", "Node", or "Pod")

- **units-count**: (uint) number of GPUs

- **links-count**: (uint) number of links

- **link-latency**: (uint) link latency (ns)

- **link-bandwidth**: (uint) link bandwidth (GB/s or B/ns)

- **nic-latency**: (uint) nic latency (ns)

- **router-latency**: (uint) router latency (ns)

- **hbm-latency**: (uint) memory latency (ns)

- **hbm-bandwidth**: (uint) memory bandwidth (GB/s or B/ns)

- **hbm-scale**: (uint) memory scaling factor

## [Garnet Network Config](https://github.com/astra-sim/astra-network-garnet/tree/c09ba4ebee0643cff3f75d64143d5310b7f31ee1)

Example network configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/inputs/network/garnet/
:::

- **num-npus**: (int) Total number of NPUs we are simulating

- **num-packages**: (int) Total number of packages (each could contain one or multiple NPUs)

- **package-rows**: (int) Number of package rows. it defines the vertical dimension size

- **topology**: (NV_Switch/Torus3D) Determines the physical topology

- **local-rings**: (int) Determines the number of rings in the local (intra-package) dimension

- **vertical-rings**: (int) Determines the number of rings in the vertical (inter-package) dimension (applicable only on the Torus3D topology)

- **horizontal-rings**: (int) Determines the number of rings in the horizontal (inter-package) dimension (applicable only on the Torus3D topology)

- **links-per-tile**: (int) Determines the number of links for the alltoall (inter-package) dimesnion (applicable only on the NV_Switch topology)

- **flit-width**: (int) The width of flits in bits

- **local-packet-size**: (int) The size of intra-pcakge packets in bytes

- **package-packet-size**: (int) The size of inter-pcakge packets in bytes

- **tile-link-width**: (int) The width of intra-pcakge links in bits

- **package-link-width**: (int) The width of inter-pcakge links in bits

- **vcs-per-vnet**: (int) Number of VCs per each Vnet

- **routing-algorithm**: (Ring_XY/AllToAll) Routing algorithm

- **router-latency**: (int) Delay at each router

- **local-link-latency**: (int) delay of intra-package links in cycles

- **package-link-latency**: (int) delay of inter-package links in cycles

- **buffers-per-vc**: (int) Buffer size per each VS in terms of number of flits

- **local-link-efficiency**: (float) The ratio of (data/header+data) for intra-package packets

- **package-link-efficiency**: (float) The ratio of (data/header+data) for inter-package packets

## [NS3 Network Config](https://github.com/astra-sim/astra-network-ns3/tree/a46d80f9fab4d44ba687e81588c9d317ecaf3370)

Example network configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/inputs/network/ns3/
:::
