# Installation

## Install Dependencies
For Debian-based Linux distributions (including Ubuntu), you can install ASTRA-sim dependencies by executing the following commands.
:::{code-block} console
$ sudo apt update
$ sudo apt install \
  gcc g++ make cmake \
  libboost-dev libboost-program-options-dev \
  libprotobuf-dev protobuf-compiler \
  python3 python3-pip git
$ sudo pip3 install protobuf==3.6.1 pydot
:::

## Compile ASTRA-sim
:::{note}
Please make sure that you have all the required depencencies installed.
:::

1. To install ASTRA-sim, clone it from GitHub:

:::{code-block} console
$ git clone --recurse-submodules git@github.com:astra-sim/astra-sim.git
:::

2. After that, go to the downloaded directory and execute the build script based on your target network backend:

:::{code-block} console
$ cd astra-sim

# For the analytical network backend
$ ./build/astra_analytical/build.sh
:::
