# Setup ASTRA-Sim - Installation

## Clone Repository

:::{code-block} console
git clone git@github.com:astra-sim/astra-sim.git
ASTRA_SIM=$(realpath ./astra-sim)
cd ${ASTRA_SIM}
git submodule update --init --recursive
:::

## Docker Setup (Recommended)

Build Docker Image

:::{code-block} console  
docker build -t astra-sim:latest -f Dockerfile .
:::

Run Docker Container

:::{code-block} console  
docker run -it --name astra-sim-latest  --shm-size=8g astra-sim:latest bash
:::

## Bare Metal Deployment Dependencies

### Debian-Based Linux Distributions (Recommend Ubuntu 22.04)

Install system dependencies:

:::{code-block} console  
sudo apt -y update
sudo apt -y install coreutils wget vim git
sudo apt -y install gcc-11 g++-11 make cmake 
sudo apt -y install clang-format 
sudo apt -y install libboost-dev libboost-program-options-dev
sudo apt -y install python3.10 python3-pip
sudo apt -y install libprotobuf-dev protobuf-compiler
sudo apt -y install openmpi-bin openmpi-doc libopenmpi-dev
:::

Install Python packages:

:::{code-block} console  
pip3 install --upgrade pip
pip3 install protobuf==5.28.2
pip3 install graphviz pydot
:::


