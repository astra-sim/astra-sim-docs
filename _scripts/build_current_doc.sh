#!/bin/bash
set -e

# Cleanup Current Build, if one exists
rm -rf ./_build

# Compile the latest version
sphinx-build \
    -b html \
    -j $(nprocs) \
    -d ./_build/doctree \
    . ./_build/html
