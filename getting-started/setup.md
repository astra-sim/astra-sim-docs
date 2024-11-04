# Dependencies Setup

## Debian-Based Linux Distributions

Install required system packages:

:::{code-block} console
$ sudo apt update
$ sudo apt install \
  gcc g++ make cmake \
  libboost-dev libboost-program-options-dev \
  libprotobuf-dev protobuf-compiler \
  openmpi-bin openmpi-doc libopenmpi-dev \
  python3 python3-pip git
:::

Then, you need to install protobuf. We recommand you to use protobuf 3.6.1. 
You can download protobuf 3.6.1 here: [[GitHub]](https://github.com/protocolbuffers/protobuf/releases/tag/v3.6.1) [[protobuf-all-3.6.1.tar.gz]](https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-all-3.6.1.tar.gz).

:::{code-block} console
# Installing protobuf 3.6.1 locally
$ ./configure
$ make -j$(nproc)
$ make check -j$(nproc)  # checking compilation finished successfully
$ sudo make install  # register protobuf to PATH
$ which protoc  # system should be able to locate protoc
$ protoc --version  # should be 3.6.1
:::

Now, you can install required Python packages, either through conda or pip3:

- ### Conda

If you are managing Python environments through conda, you can run below commands to create a new environment for astra-sim.

:::{code-block} console
$ conda create -n astra-sim python=3.7
$ conda activate astra-sim
$ conda install graphviz python-graphviz pydot
:::

- ### pip3

You can also install required Python packages natively using pip3.

:::{code-block} console
$ pip3 install --upgrade pip
$ pip3 install pydot
:::

## macOS using [homebrew](https://brew.sh/)

:::{code-block} console
$ brew update
$ brew upgrade
$ brew install boost cmake coreutils
:::

Then, you have to install protobuf 3.6.1 locally. You can download protobuf 3.6.1 here: [[GitHub]](https://github.com/protocolbuffers/protobuf/releases/tag/v3.6.1) [[protobuf-all-3.6.1.tar.gz]](https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-all-3.6.1.tar.gz).

:::{code-block} console
# Installing protobuf 3.6.1 locally
$ ./configure
$ make -j$(nproc)
$ make check -j$(nproc)  # checking compilation finished successfully
$ sudo make install  # register protobuf to PATH
$ which protoc  # system should be able to locate protoc
$ protoc --version  # should be 3.6.1
:::

## Windows

ASTRA-sim is not natively supporting Windows environment at this moment. We suggest to use Docker or [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)).

