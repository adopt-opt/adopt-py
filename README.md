# 🤖🌊🚀 AI-Driven Design and Optimization (ADOPT)

## About

Python package for AI-driven design and optimization of scientific simulators building on

* 📈 [Ray](https://www.ray.io) for parallelization, [auto-scaling](https://docs.ray.io/en/latest/cluster/getting-started.html), and [auto-tuning](https://docs.ray.io/en/latest/tune/index.html)
* 🤖 [Vizier Service](https://github.com/google/vizier) to keep track of the optimization configurations

Belied by a metadata system guaranteeing the physical correctness of configurations, and employing an SMT-solver to solve for allowed configurations of solvers, and optimization algorithms.

## Installation

To get the full repository you have to either recursively clone the repository with its submodules

```bash
git clone --recursive https://github.com/adopt-opt/adopt-py
```

or if you already have an `adopt-py` download, initialize the submodules

```bash
git submodule update --init --recursive
```

To then set up the [conda](https://conda.io/projects/conda/en/latest/index.html) environment we use the [environment.yml](./environment.yml):

```bash
conda env create -f environment.yml
```

The `adopt-py` package itself can then be installed with:

```bash
pip install .
```

> For package development you also need to install [requirements-dev.txt](./requirements-dev.txt) with `pip install -r requirements-dev.txt`.

## Packaged Components

### Solvers

### Design ptimization Algorithms
