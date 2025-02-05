# Argument ${NETWORK_CONFIG}

:::{code-block} console
--network-configuration: path to the network configuration file
:::

## [Analytical Network Config](https://github.com/astra-sim/astra-network-analytical/tree/40d3d0ff11bfd241b20423f1d9b5c670dc0d5bd8)

Example network configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/examples/network_analytical/network.yml
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
$ ${ASTRA_SIM}/extern/network_backend/ns-3/scratch/config/
:::

The Network configuration file defines the knobs to the ns3 simulation.  
Refer to [this spreadsheet](https://docs.google.com/spreadsheets/d/1Xoo_QWgOuEJojnCOv-znwzARLjFArlR6tULKA2CBIqQ/edit?usp=sharing) for a detailed description of each knobs. 

### Physical Topology
One important knob of the configuration is the *physical topology*. Examples are located in `.../ns-3/scratch/topology`, and the filenames are defined in the configuration file under `TOPOLOGY_FILE`.

Let's take a sample file, `7_nodes_3_switch_topology.txt`, and examine its components. This file describes a topology where there are 7 nodes, 3 of which are network switches (4, 5, 6). There are 8 links in total. 

```
7 3 8 // {no. of nodes}  {no. of switches}  {no. of links}
4 5 6 // {List of node id for switches}
4 0 200Gbps 0.0005ms 0 // From here on each line corresponds to one link.
6 0 200Gbps 0.0005ms 0 // {id of one endpoint} {id of another endpoint} {bandwidth} {latency} {error rate of link}
4 1 200Gbps 0.0005ms 0
6 1 200Gbps 0.0005ms 0
5 2 200Gbps 0.0005ms 0
6 2 200Gbps 0.0005ms 0
5 3 200Gbps 0.0005ms 0
6 3 200Gbps 0.0005ms 0

```

### Logical Topology 
In addition to the ns3 configurations (including the physical topology), the binary for the NS3 backend takes a unique command line argument, `--logical-topology-configuration=${LOGICAL_TOPOLOGY}`. 

Examples of this can be found at 

:::{code-block} console
$ ${ASTRA_SIM}/examples/ns3/sample_64nodes_2D.json
:::

This file defines the *logical* topology, where each number corresponds to the number of NPUs in a dimension.
If the file shows `{8, 4}`, the system layer will run a 2D topology, regardless of the physical connectivity.
