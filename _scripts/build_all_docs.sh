#!/bin/bash
set -e

# Cleanup Current Build, if one exists
rm -rf ./_build

# Get Versions
versions=($(git tag))

# Compile the latest version
sphinx-build \
    -b html \
    -j$(nproc) \
    -D version="latest" \
    -d ./_build/doctree \
    . ./_build/html

# Compile Each Version
for version in "${versions[@]:?}"; do
    # Checkout to specific version
    echo "Compiling version ${version:?}"
    git checkout "${version:?}"

    # Compile
    sphinx-build \
        -b html \
        -j$(nproc) \
        -D version="${version:?}" \
        -d ./_build/doctree \
        . ./_build/html/"${version:?}"
done

# Return to the latest branch
git checkout main
