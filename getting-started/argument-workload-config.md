# Argument ${WORKLOAD_CONFIG}

:::{code-block} console
--workload-configuration: path to the prefix of execution trace files
:::

The example traces can be found at:
:::{code-block} console
${ASTRA_SIM}/inputs/workload/
:::

:::{note}
The naming rule for execution traces follows the format {path_prefix}.{npu_id}.et.
:::

## Using [Chakra Execution Trace](https://github.com/mlcommons/chakra/wiki)
ASTRA-sim supports Chakra ET (Execution Trace) as inputs to the workload layer. 

An example of how to generate Chakra traces and run ASTRA-sim is illustrated at [Running Simulation with Chakra](https://github.com/mlcommons/chakra/wiki/Running-Simulation-with-Chakra). 

## Using Execution Trace Converter (et_converter)
You can convert ASTRA-sim 1.0 text input files into Chakra traces with the following commands.
```bash
$ cd ./extern/graph_frontend/chakra/
$ pip3 install .
$ python3 -m chakra.et_converter.et_converter \
    --input_type Text \
    --input_filename ../../../inputs/workload/ASTRA-sim-1.0/Resnet50_DataParallel.txt \
    --output_filename ../../../inputs/workload/ASTRA-sim-2.0/Resnet50_DataParallel \
    --num_npus 64 \
    --num_dims 1 \
    --num_passes 1
```

Run the following command.
```bash
$ cd -
$ ./build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Unaware \
  --workload-configuration=./inputs/workload/ASTRA-sim-2.0/Resnet50_DataParallel \
  --system-configuration=./inputs/system/Switch.json \
  --network-configuration=./inputs/network/analytical/Switch.yml \
  --remote-memory-configuration=./inputs/remote_memory/analytical/no_memory_expansion.json
```

Upon completion, ASTRA-sim will display the number of cycles it took to run the simulation.
```bash
sys[62] finished, 6749042 cycles
sys[61] finished, 6749042 cycles
...
sys[0] finished, 6749042 cycles
sys[63] finished, 6749042 cycles
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
