# Validation on GPU Systems - NCCL over HGX-H100 Systems

## HGX-H100 Topology
![alt text](../../_static/images/validation/hardware/hgx_h100/hgx_h100_topology.png)

## Senario - 1: 2-GPUs All-Reduce
### Hardware Setup
1. 2 H100 GPUs connected in switch, over 4 NVSwitches
2. Each GPU has bidirectional BW of 900 GB/s
3. NCCL Ring Algorithm

### ASTRA-Sim setup
1. Modelled with the ASTRA-Sim Analytical Backend
2. Switch Network Topology

### Collectives run
1. All-Reduce
2. Reduction operation - Sum


### Results
![alt text](../../_static/images/validation/hardware/hgx_h100/2gpus.png)

**Geomean error rate = 20.63%**


## Senario - 2: 4-GPUs All-Reduce
### Hardware Setup
1. 4 H100 GPUs connected in switch, over 4 NVSwitches
2. Each GPU has bidirectional BW of 900 GB/s
3. NCCL Ring Algorithm

### ASTRA-Sim setup
1. Modelled with the ASTRA-Sim Analytical Backend
2. Switch Network Topology

### Collectives run
1. All-Reduce
2. Reduction operation - Sum

### Results
![alt text](../../_static/images/validation/hardware/hgx_h100/4gpus.png)

**Geomean error rate = 12.01%**

## Senario - 3: 8-GPUs All-Reduce
### Hardware Setup
1. 8 H100 GPUs connected in switch, over 4 NVSwitches
2. Each GPU has bidirectional BW of 900 GB/s
3. NCCL Ring Algorithm

### ASTRA-Sim setup
1. Modelled with the ASTRA-Sim Analytical Backend
2. Switch Network Topology

### Collectives run
1. All-Reduce
2. Reduction operation - Sum

### Results
![alt text](../../_static/images/validation/hardware/hgx_h100/8gpus.png)

**Geomean error rate = 9.69%**


## Recommended practices
1. Emperically extract warm up latency by running smaller collectives
2. Emperically extract practical link latency by first running smaller collectives and varying number of NPUs/GPUs
3. It is observed that the maximum achieved BW is 741.34 GB/s (bidirectional).
4. Strictly enforce NCCL to use only Ring Algorithm. NCCL switches from Ring to Tree algorithm with respect to Collective sizes. We observe this to be suboptimal, atleast for this topology, hardware and configuration.