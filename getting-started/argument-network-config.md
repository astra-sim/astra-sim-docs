# Argument ${NETWORK_CONFIG}

:::{code-block} console
--network-configuration: path to the network configuration file
:::

## [Analytical Network Config](https://github.com/astra-sim/astra-network-analytical)

Example network configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/examples/network/analytical/Ring_8npus.yml
:::

The analytical network configuration uses a simple YAML format:

```yaml
topology: [ Ring ]
npus_count: [ 8 ]
bandwidth: [ 50.0 ]  # GB/s
latency: [ 500.0 ]   # ns
```

- **topology**: (array) network topology per dimension — options: `Ring`, `FullyConnected`, `Switch`
- **npus_count**: (array) number of NPUs per dimension
- **bandwidth**: (array) link bandwidth per dimension in GB/s
- **latency**: (array) link latency per dimension in ns

:::{note}
Each array is indexed by dimension level. For a 2D topology, each array would have two entries (one per dimension).
:::

For more details, see the [Analytical Network Simulator Documentation](https://astra-sim.github.io/astra-network-analytical-docs/index.html).

## [Garnet Network Config](https://github.com/astra-sim/astra-network-garnet)

:::{warning}
The Garnet backend is no longer actively maintained in the current version of ASTRA-sim.
The configuration fields below are preserved for reference but may not work with the latest codebase.
:::

- **num-npus**: (int) Total number of NPUs we are simulating

- **num-packages**: (int) Total number of packages (each could contain one or multiple NPUs)

- **package-rows**: (int) Number of package rows. it defines the vertical dimension size

- **topology**: (NV_Switch/Torus3D) Determines the physical topology

- **local-rings**: (int) Determines the number of rings in the local (intra-package) dimension

- **vertical-rings**: (int) Determines the number of rings in the vertical (inter-package) dimension (applicable only on the Torus3D topology)

- **horizontal-rings**: (int) Determines the number of rings in the horizontal (inter-package) dimension (applicable only on the Torus3D topology)

- **links-per-tile**: (int) Determines the number of links for the alltoall (inter-package) dimension (applicable only on the NV_Switch topology)

- **flit-width**: (int) The width of flits in bits

- **local-packet-size**: (int) The size of intra-package packets in bytes

- **package-packet-size**: (int) The size of inter-package packets in bytes

- **tile-link-width**: (int) The width of intra-package links in bits

- **package-link-width**: (int) The width of inter-package links in bits

- **vcs-per-vnet**: (int) Number of VCs per each Vnet

- **routing-algorithm**: (Ring_XY/AllToAll) Routing algorithm

- **router-latency**: (int) Delay at each router

- **local-link-latency**: (int) delay of intra-package links in cycles

- **package-link-latency**: (int) delay of inter-package links in cycles

- **buffers-per-vc**: (int) Buffer size per each VC in terms of number of flits

- **local-link-efficiency**: (float) The ratio of (data/header+data) for intra-package packets

- **package-link-efficiency**: (float) The ratio of (data/header+data) for inter-package packets

## [NS-3 Network Config](https://github.com/astra-sim/astra-network-ns3)

Example network configurations can be found at

:::{code-block} console
$ ${ASTRA_SIM}/extern/network_backend/ns-3/scratch/config/
:::

The Network configuration file defines the knobs to the ns3 simulation.  
Refer to [this spreadsheet](https://docs.google.com/spreadsheets/d/1Xoo_QWgOuEJojnCOv-znwzARLjFArlR6tULKA2CBIqQ/edit?usp=sharing) for a detailed description of each knobs. 

### Physical Topology
One important knob of the configuration is the *physical topology*. Examples are located in `.../ns-3/scratch/topology`, and the filenames are defined in the configuration file under `TOPOLOGY_FILE`.

Let's take a sample file, `8_nodes_1_switch_topology.txt`, and examine its components. The file format is:

- Line 1: `{no. of nodes} {no. of switches} {no. of links}`
- Line 2: `{List of node IDs for switches}`
- Each subsequent line: `{id of one endpoint} {id of another endpoint} {bandwidth} {latency} {error rate of link}`

Available topology examples in `extern/network_backend/ns-3/scratch/topology/`:
- `8_nodes_1_switch_topology.txt`
- `8nodes_ring_topology.txt`
- `128_nodes_16_switch_topology.txt`
- `128_nodes_32_switch_topology.txt`

### Logical Topology 
In addition to the ns3 configurations (including the physical topology), the binary for the NS3 backend takes a unique command line argument, `--logical-topology-configuration=${LOGICAL_TOPOLOGY}`. 

Examples of this can be found at

:::{code-block} console
$ ${ASTRA_SIM}/examples/network/ns3/sample_16nodes_2D.json
:::

Available logical topology examples:
- `sample_4nodes_1D.json` — 4 NPUs, 1D
- `sample_8nodes_1D.json` — 8 NPUs, 1D
- `sample_16nodes_1D.json` — 16 NPUs, 1D
- `sample_16nodes_2D.json` — 16 NPUs, 2D

This file defines the *logical* topology, where each number corresponds to the number of NPUs in a dimension.
If the file shows `{8, 4}`, the system layer will run a 2D topology, regardless of the physical connectivity.
