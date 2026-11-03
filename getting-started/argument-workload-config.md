# Argument ${WORKLOAD_CONFIG}

:::{code-block} console
--workload-configuration: path to the prefix of execution trace files
:::

The example traces can be found at:
:::{code-block} console
${ASTRA_SIM}/examples/workload/microbenchmarks/
:::

Available microbenchmarks:
- `all_reduce/{4,8,16}npus_1MB/` — AllReduce collectives
- `all_gather/{4,8,16}npus_1MB/` — AllGather collectives
- `reduce_scatter/{4,8,16}npus_1MB/` — ReduceScatter collectives
- `all_to_all/{4,8,16}npus_1MB/` — AllToAll collectives

:::{note}
The naming rule for execution traces follows the format {path_prefix}.{npu_id}.et.
:::

## Using [Chakra Execution Trace](https://github.com/mlcommons/chakra/wiki)
ASTRA-sim supports Chakra ET (Execution Trace) as inputs to the workload layer. 

To run a preset workload, use the example run scripts:
```bash
cd ${ASTRA_SIM}/examples/run_scripts/analytical/congestion_aware
bash Ring_allgather_16npus.sh
```

This script compiles ASTRA-Sim, runs an all-gather workload on 16 NPUs connected in a ring topology, and displays the number of cycles required to complete the simulation.

This script will compile ASTRA-Sim, run the workload on an 8-NPU cluster, and display the number of cycles required to complete the simulation.
```bash
[2025-01-26 23:03:37.384] [workload] [info] sys[0] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[1] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[2] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[3] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[4] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[5] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[6] finished, 64440 cycles, exposed communication 64440 cycles.
[2025-01-26 23:03:37.384] [workload] [info] sys[7] finished, 64440 cycles, exposed communication 64440 cycles.
```

An example of how to generate Chakra traces and run ASTRA-sim is illustrated at [Running Simulation with Chakra](https://github.com/mlcommons/chakra/wiki/Running-Simulation-with-Chakra). 

## Using Execution Trace Converter
You can convert ASTRA-sim 1.0 text input files into Chakra traces using the text converter in the Chakra submodule.
```bash
$ cd ./extern/graph_frontend/chakra/
$ pip3 install .
```

Then use the text converter to generate Chakra ET files from your workload description. For generating synthetic ETs for realistic workloads (including both compute and communication), you can also use [STG (Symbolic Tensor Graph)](https://github.com/astra-sim/symbolic_tensor_graph).

Once you have Chakra ET files, run ASTRA-sim with the correct configuration paths:
```bash
$ ./build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Aware \
  --workload-configuration=./examples/workload/microbenchmarks/all_reduce/8npus_1MB/all_reduce \
  --system-configuration=./examples/system/native_collectives/Ring_4chunks.json \
  --network-configuration=./examples/network/analytical/Ring_8npus.yml \
  --remote-memory-configuration=./examples/remote_memory/analytical/no_memory_expansion.json
```

Upon completion, ASTRA-sim will display the number of cycles it took to run the simulation.
```bash
[2025-01-26 22:50:05.669] [workload] [info] sys[0] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[1] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[2] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[3] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[4] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[5] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[6] finished, 1082478600 cycles, exposed communication 28600 cycles.
[2025-01-26 22:50:05.669] [workload] [info] sys[7] finished, 1082478600 cycles, exposed communication 28600 cycles.
```
