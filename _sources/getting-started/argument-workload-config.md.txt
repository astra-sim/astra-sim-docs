# Argument ${WORKLOAD_CONFIG}

:::{code-block} console
--workload-configuration: path to the prefix of execution trace files
:::

The naming rule for execution traces follows the format {path_prefix}.{npu_id}.et.

:::{note}
Execution traces can be created using [Chakra tools](https://github.com/mlcommons/chakra/blob/main). You have the option of using either execution trace generator (et_generator) or execution trace converter (et_converter).
:::

## Using Execution Trace Generator (et_generator)

et_generator can be used to define and generate any execution traces, functioning as a test case generator. You can generate execution traces with the following commands:

:::{code-block} console
$ cd ${ASTRA_SIM}/extern/graph_frontend/chakra/et_generator
$ cmake CMakeLists.txt && make -j$(nproc)
$ ./et_generator --num_npus 64 --num_dims 1
:::

To run one of the example traces (oneCommNodeAllReduce), execute the following command:

:::{code-block} console
$ cd -
$ ./build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Unaware \
  --workload-configuration=./extern/graph_frontend/chakra/et_generator/oneCommNodeAllReduce \
  --system-configuration=./inputs/system/Switch.json \
  --network-configuration=./inputs/network/analytical/Switch.yml \
  --remote-memory-configuration=./inputs/remote_memory/analytical/no_memory_expansion.json
  
# For the ns3 network backend. Python2 required
# After editing the configuration files in the following script
$ ./build/astra_ns3/build.sh -r

# Or, alternatively:
$ cd ./extern/network_backend/ns3/simulation
$ ./waf --run "scratch/AstraSimNetwork \
  --workload-configuration=../../../../extern/graph_frontend/chakra/et_generator/oneCommNodeAllReduce \
  --system-configuration=../../../../inputs/system/Switch.json \
  --network-configuration=mix/config.txt \
  --remote-memory-configuration=../../../../inputs/remote_memory/analytical/no_memory_expansion.json \
  --logical-topology-configuration=../../../../inputs/network/ns3/sample_64nodes_1D.json \
  --comm-group-configuration=\"empty\""
$ cd -

:::

Upon completion, ASTRA-sim will display the number of cycles it took to run the simulation.

:::{code-block} console
:lineno-start: 1

sys[0] finished, 50904 cycles
sys[1] finished, 50904 cycles
...
sys[62] finished, 50904 cycles
sys[63] finished, 50904 cycles
:::

## Using Execution Trace Converter (et_converter)

et_converter is a trace schema conversion tool, supporting PyTorch and FlexFlow execution traces, as well as ASTRA-sim 1.0 input files. You can convert ASTRA-sim 1.0 text input files into Chakra traces with the following commands:

:::{code-block} console
$ cd ${ASTRA_SIM}/extern/graph_frontend/chakra/
$ python3 setup.py install --user
$ python3 -m et_converter.et_converter \
  --input_type Text \
  --input_filename ../../../inputs/workload/ASTRA-sim-1.0/Resnet50_DataParallel.txt \
  --output_filename ../../../inputs/workload/ASTRA-sim-2.0/Resnet50_DataParallel \
  --num_npus 64 \
  --num_dims 1 \
  --num_passes 1
:::

Run the following command:

:::{code-block} console
$ cd -
$ ./build/astra_analytical/build/bin/AstraSim_Analytical_Congestion_Unaware \
  --workload-configuration=./inputs/workload/ASTRA-sim-2.0/Resnet50_DataParallel \
  --system-configuration=./inputs/system/Switch.json \
  --network-configuration=./inputs/network/analytical/Switch.yml \
  --remote-memory-configuration=./inputs/remote_memory/analytical/no_memory_expansion.json

# Similarly, for ns3, run the previous command while only changing the workload.
:::

Upon completion, ASTRA-sim will display the number of cycles it took to run the simulation.

:::{code-block} console
:lineno-start: 1
sys[62] finished, 6749042 cycles
sys[61] finished, 6749042 cycles
...
sys[0] finished, 6749042 cycles
sys[63] finished, 6749042 cycles
:::
