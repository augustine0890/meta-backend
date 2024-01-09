# Project Template
A demonstration of a (relatively) complete solution with test cases, and documentation.

## Installation
This isn't installed with PIP, Instead, checkout the Github repository.
After checkout, use the `requirements-dev.txt` to install the needed development components.
`python -m pip install -r requirements-dev.txt`

## Building an Initial Python Environment
One way to get started is to use Conda to build the environment. Conda can be downloaded via the Miniconda installer. See https://docs.conda.io/projects/miniconda/en/latest/
Then the following conda commands will populate enough Python (and tools) to build an environment
`conda create -n myproject python=3.11`
- To activate this environment, use
`conda activate projecttemplate`
`conda install --channel=conda-forge pip-tools`
- To deactivate an active environment, use
`conda deactivate`

With the pip-compile command, the list of required packages in the `pyproject.toml` can be turned into a complete list of packages to install.
`pip-compile --all-extras -o requirements-dev.txt`
`pip install -r requirements-dev.txt`
`pip-compile --extra=test --output-file=requirements-test.txt`