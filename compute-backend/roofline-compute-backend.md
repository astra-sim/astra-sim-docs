# Roofline Compute Backend

:::{note}
This page is currently under construction. Please stay tuned for updates!
:::

## Enable Roofline Models
ASTRA-sim 2.0 supports two computational performance models: the measured runtime model and the roofline model. You can enable the roofline model by setting the 'roofline-enabled' field to 1 in the system configuration file. Additionally, specify the local memory bandwidth (in GB/sec) and peak performance (in TFLOPS).
```
...
"roofline-enabled": 1,
"local-mem-bw": 50,
"peak-perf": 2000,
...
```
When creating execution traces, ensure to include the number of floating point operations and the tensor size for each compute operator.
