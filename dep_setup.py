import sys

import pypigeonhole_build.pip_dep_utils as pip_dep_utils
from pypigeonhole_build.pip_dep_utils import INSTALL, DEV, PIP, Dependency

import pypigeonhole_build.conda_dep_utils as conda_dep_utils
from pypigeonhole_build.conda_dep_utils import CONDA

CONDA.env = 'py385_pt'  # change to your environment name
CONDA.channels = ['defaults']  # update channels, if needed.

dependent_libs = [
    # your dependencies here

    Dependency(name='pypigeonhole-build'),

    Dependency(name='python', version='>=3.5', scope=INSTALL, installer=CONDA),
    Dependency(name='coverage', version='==5.3', installer=CONDA, desc='test coverage'),  # DEV
    Dependency(name='pipdeptree'),  # latest version, DEV, PIP. Conda does not have these 2
    Dependency(name='coverage-badge', scope=DEV, installer=PIP),  # generate coverage github badge
]

install_required = pip_dep_utils.get_install_required(dependent_libs)

test_required = pip_dep_utils.get_test_required(dependent_libs)

python_requires = pip_dep_utils.get_python_requires(dependent_libs)

if __name__ == "__main__":
    if len(sys.argv) >= 2:  # This is to print env name to shell so conda activates this env.
        print(CONDA.env)
    else:  # This generates environment.yaml for conda to create new environment
        conda_dep_utils.gen_conda_yaml(dependent_libs, './environment.yaml')
