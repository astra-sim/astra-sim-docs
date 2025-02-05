# Argument ${WORKLOAD_CONFIG}

:::{code-block} console
--workload-configuration: path to the prefix of execution trace files
:::

The example traces can be found at:
:::{code-block} console
${ASTRA_SIM}/examples/network_analytical/workload
:::

:::{note}
The naming rule for execution traces follows the format {path_prefix}.{npu_id}.et.
:::

## Using [Chakra Execution Trace](https://github.com/mlcommons/chakra/wiki)
ASTRA-sim supports Chakra ET (Execution Trace) as inputs to the workload layer. 

To run a preset workload, such as `AllReduce_1MB`, execute the following commands:
```bash
cd ${ASTRA_SIM}/examples/network_analytical
bash run_network_analytical.sh
```

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

## Using Execution Trace Converter (et_converter)
You can convert ASTRA-sim 1.0 text input files into Chakra traces with the following commands.
```bash
$ cd ./extern/graph_frontend/chakra/
$ pip3 install .
$ chakra_converter Text \
    --input ../../../examples/text_converter/text_workloads/Resnet50_DataParallel.txt \
    --output ../../../examples/text_converter/text_workloads/Resnet50_DataParallel \
    --num-npus 8 \
    --num-passes 1
```

In the project root, run the following command.
```bash
$ ./build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Unaware \
  --workload-configuration=./examples/text_converter/text_workloads/Resnet50_DataParallel \
  --system-configuration=./examples/text_converter/system.json \
  --network-configuration=./examples/text_converter/network.yml \
  --remote-memory-configuration=./examples/text_converter/remote_memory.json
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

## Enable Communicator Groups
ASTRA-sim 2.0 supports [communicator groups](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/communicators.html).
You can pass a communicator group configuration file by specifying the file path using `--comm-group-configuration`.
If you do not pass a communicator group configuration file, by default, it will create a single group with all GPUs.
A valid communication group file is a JSON file with the following format.
```
{
  "<communicator_group_id>" : [gpu_ids]
}
```
For example, you can create two communicator groups with the following configuration file.
The first communicator group, with ID 0, includes GPU IDs from 0 to 3. The second communicator group, with ID 1, includes GPU IDs from 4 to 7.
```
{
  "0": [0, 1, 2, 3],
  "1": [4, 5, 6, 7]
}
```
