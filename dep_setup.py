import sys

from bin.dep_setup_utils import CONDA, Dependency, INSTALL
from bin import dep_setup_utils

CONDA.env = 'py385_t1'  # change to your environment name
CONDA.channels = ['defaults']  # update channels, if needed.

dependent_libs = [
    # your dependencies here

    Dependency(name='python', version='==3.8.5', scope=INSTALL, installer=CONDA),
    Dependency(name='coverage', version='==5.3', installer=CONDA, desc='test coverage'),  # DEV
    Dependency(name='pipdeptree'),  # latest version, DEV, PIP. Conda does not have these 2
    Dependency(name='coverage-badge'),
]

install_required = dep_setup_utils.get_install_required(dependent_libs)

test_required = dep_setup_utils.get_test_required(dependent_libs)

if __name__ == "__main__":
    if len(sys.argv) >= 2:  # This is to print env name to shell so conda activates this env.
        print(CONDA.env)
    else:  # This generates environment.yaml for conda to create new environment
        dep_setup_utils.gen_conda_yaml(dependent_libs)
