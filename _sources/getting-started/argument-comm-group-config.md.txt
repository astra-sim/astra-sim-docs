# Argument {COMM_GROUP_CONFIG}

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

When simulating the workload, ASTRA-sim looks for the communication group id in each communication ET node (i.e. different operators of the same rank may have different communicator group). ASTRA-sim will look for the attribute `pg_name` in the communication ET node. 

The following is *part* of a Chakra ET. 
```json
{
  "id": "4",
  "name": "in_emb_y@0_X1COMM",
  "type": "COMM_COLL_NODE",
  "attr": [
    {
      "name": "comm_size",
      "int64Val": "26843545600"
    },
    {
      "name": "comm_type",
      "int64Val": "2"
    },
    {
      "name": "pg_name",
      "stringVal": "17"
    },
    {
      "name": "is_cpu_op",
      "int32Val": 0
    }
  ]
}
```
