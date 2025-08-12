# ASTRA-Sim: Quick Example


Run Astra-Sim with a quick example ([Ring_allgather_16npus.sh](https://github.com/astra-sim/astra-sim/blob/master/examples/run_scripts/analytical/congestion_aware/Ring_allgather_16npus.sh)): 
This example demonstrates a ring all-gather operation on 16 NPUs connected in a ring topology. Please go back to build up the necessary dependencies before running the example.
The following shows the expected output:
:::{code-block} console
:lineno-start: 1

[system::topology::RingTopology] [info] ring of node 0, id: 0 dimension: local total nodes in ring: 16 index in ring: 0 offset: 1 total nodes in ring: 16
[system::topology::RingTopology] [info] ring of node 0, id: 0 dimension: local total nodes in ring: 16 index in ring: 0 offset: 1 total nodes in ring: 16
[system::topology::RingTopology] [info] ring of node 0, id: 0 dimension: local total nodes in ring: 16 index in ring: 0 offset: 1 total nodes in ring: 16
[system::topology::RingTopology] [info] ring of node 0, id: 0 dimension: local total nodes in ring: 16 index in ring: 0 offset: 1 total nodes in ring: 16
[workload] [info] sys[12] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[13] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[14] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[15] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[0] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[1] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[2] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[3] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[4] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[5] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[6] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[7] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[8] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[9] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[10] finished, 323560 cycles, exposed communication 323560 cycles.
[workload] [info] sys[11] finished, 323560 cycles, exposed communication 323560 cycles.
:::


For additional quick runs and other featured microbenchmarks, see the [ASTRA-Sim Examples](https://github.com/astra-sim/astra-sim/tree/master/examples) and review the accompanying documentation.