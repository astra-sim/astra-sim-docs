# Build ASTRA-sim

:::{note}
Please make sure that you have all the required depencencies installed.
:::

## Clone Repository

```bash
$ git clone --recurse-submodules git@github.com:astra-sim/astra-sim.git
$ cd astra-sim
```

## Build with Docker (Optional)

```bash
# Create Docker Image
$ docker build -t astra-sim .

# Run Docker Image
$ docker run -it astra-sim
```

## Compile Program

```bash
# For Analytical Network Backend
$ ./build/astra_analytical/build.sh

# For NS3 Network Backend
$ ./build/astra_ns3/build.sh -c
```

