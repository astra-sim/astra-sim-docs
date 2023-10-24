# astra-sim-docs
ASTRA-sim Documentation

| main branch | Status |
|:---:|:---:|
| build | [![build](https://github.com/astra-sim/astra-sim-docs/actions/workflows/check_build_status.yml/badge.svg)](https://github.com/astra-sim/astra-sim-docs/actions/workflows/check_build_status.yml) |
| deploy | [![deploy](https://github.com/astra-sim/astra-sim-docs/actions/workflows/deploy_docs.yml/badge.svg)](https://github.com/astra-sim/astra-sim-docs/actions/workflows/deploy_docs.yml) |


## Dependencies
This documentation uses `sphinx` documentation generator and `read the docs` sphinx theme. In order to compile the documentation, please install such dependencies through Python (`pip3`). You may consider creating a virtual environment through `conda`.

### Create a Conda Environment (If Desired)
```
$ conda create -n sphinx python=3.11
$ conda activate sphinx
```

### Install Dependencies
```bash
$ pip3 install gitpython sphinx sphinx-rtd-theme myst-parser
```

## Modify the Documentation
The documentation is in Markdown (`.md`) format. Please modify the documentation as desired. `index.md` could be a good entry point and `running-astra-sim.md` can be a good reference.

Note that you might consider updating the document version defined at the beginning of the `conf.py` file. This should match the ASTRA-sim version you're documenting.


## Compile Project
With dependencies properly installed, run the script below:
```bash
$ ./_scripts/build_current_doc.sh
```

This will compile the current version of the documentation. After the compilation successfully finishes, please open `_build/html/index.html` using a web browser to check the final outcome.


## Deployement
Please open a PR to the main branch. Once merged, the documentation will be deployed automatically [https://astra-sim.github.io/astra-sim-docs/index.html](https://astra-sim.github.io/astra-sim-docs/index.html).


## Versioning
The latest HEAD commit of the main branch will be compiled and deployed as a `latest` version. If you tag a commit, it will also be automatically compiled and deployed (e.g., if a commit is tagged as `1.3`, that commit will be compiled as version `1.3` and included in the deployed website). This should all happen automatically by the GitHub Actions during the deployment phase.
