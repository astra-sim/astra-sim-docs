# Input Files for Collective API
This section describes specific pointers to the collective API within the system layer input. 
For a general description of the other items in the system layer input, please refer to the [Argument ${SYSTEM_CONFIG}](https://astra-sim.github.io/astra-sim-docs/getting-started/argument-system-config.html) page.
For a detailed explanation of the behavior of the system layer, please refer to the previous sections. 

## ASTRA-sim Native
Let's briefly take note of an example of the system layer input using the astra-sim native implementation:

```
...
  "active-chunks-per-dimension": 1,
  "all-reduce-implementation": ["ring"],
  "all-gather-implementation": ["ring", "doubleBinaryTree"],
  "all-to-all-implementation": ["ring", "doubleBinaryTree", "halvingDoubling"],
...
```

Note the values of the `all-*-implementation` items. These entries point to how the simulator will decompose the given collective into send and receive messages. Two entries in the list mean the simulator will break down the All Gather across two dimensions - the first dimension uses the ring algorithm and the second dimension uses the double binary algorithm. Note that repeated entries such as `["ring", "ring"]` are also possible. How the physical nodes are broken down into each dimension is defined by the network backend. For now, the native implementation requires that the dimensions for collective algorithsm are same across all collectives. The above example, where AllReduce is a 1D collective but AllGather is a 2D collective is simply an illustrative example. 

The mapping between each string value and the corresponding simulator code can be found in the [generate_collective_impl_from_input](https://github.com/astra-sim/astra-sim/blob/92fc71a71752f4e38d92c7d03a44829114d70143/astra-sim/system/Sys.cc#L468) function. 

## Collective API
The below is an example of the system input using the Collective API: 
```
...
    "active-chunks-per-dimension": 1,
    "all-reduce-implementation-chakra": ["/app/hoti2024/demo5/inputs/custom_ring"],
...
```

Note some differences: 
First, we use the key `all-*-implemenation-chakra` instead of `all-*-implemenation`. Note how the Chakra ET files refereed here is different from the workload file passed to the workload layer. The value in each item is the absolute path to the Chakra ET files, excluding the last `{rank}.et` string (this is similar to the Workload layer input). Also, even if there are many 'dimensions', the list only accepts one value. This is because the notion of cross-dimension communication is already included in the Chakra ET.


### Generating Chakra ET Representation from Collective Tools
We now talk about obtaining the Chakra ET files to define the collective algorithm. 

#### MSCCLang
The MSCCLang Domain Specific Language (DSL) allows users to easily and expressively write arbitrary, custom collective algorithms.
For a more detailed explanation into the MSCCLang DSL, please refer to their paper at [1]. 
First, we lower the MSCCLang DSL program into an Intermediate Representation (IR) called MSCCL-IR, which is in XML format. 
```
git clone git@github.com:jinsun-yoo/msccl-tools.git
cd msccl-tools/examples/mscclang
python3 allreduce_a100_ring.py ${NUM_GPUS} 1 1 > allreduce_ring.xml
```

Then, we convert this into a Chakra ET that ASTRA-sim's collective API can understand. 
```
git clone git@github.com:astra-sim/collectiveapi.git
cd chakra_converter

python3 et_converter.py \
    --input_type msccl \
    --input_filename ${FILEPATH}/allreduce_ring.xml \
    --output_filename allreduce_ring_mscclang \
    --coll_size 1048576

ls allreduce_ring_mscclang*
allreduce_ring_mscclang.0.et  allreduce_ring_mscclang.1.et  allreduce_ring_mscclang.2.et  allreduce_ring_mscclang.3.et
...
```
Note how we have to provide the communication size to the converter. This is a current limit where we have to hardcode the collective size into the algorithm, and ignore the collective size of the Chakra ET in the workload layer. We will release an update shortly to fix this limitation.

#### TACOS

:::{note}
This page is currently under construction. Please stay tuned for updates!
:::

**Reference**
[1] Meghan Cowan, et al. "MSCCLang: Microsoft Collective Communication Language.", In Proceedings of ASPLOS 2023, https://doi.org/10.1145/3575693.3575724
