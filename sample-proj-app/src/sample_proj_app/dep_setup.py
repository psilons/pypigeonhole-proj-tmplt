import sys
import os

import pypigeonhole_build.pip_translator as pip_translator
from pypigeonhole_build.dependency import Dependency, INSTALL, DEV, PIP

import pypigeonhole_build.conda_translator as conda_translator
from pypigeonhole_build.conda_translator import CONDA

import sample_proj_app.app_setup as app_setup

# ##############################################################################
# These are application specific information
# ##############################################################################
python_version = 'py390'  # take 3 digits, major, minor, patch

# follow same style, 3 digits, major, minor, patch
# release script is looking for this pattern: app_version =
# so don't use this pattern else where. we should have 2 assignment anyway.
app_version = "0.1.0"

CONDA.env = python_version + '_' + app_setup.get_top_pkg()
CONDA.channels = ['defaults', 'psilons']  # update channels, if needed.

dependent_libs = [
    # your dependencies here
    Dependency(name='psutil', scope=INSTALL),  # Default PIP, latest version
    Dependency(name='pypigeonhole-build', installer=CONDA),  # default scope DEV, latest version

    # development platform
    Dependency(name='python', version='>=3.6', scope=INSTALL, installer=CONDA),

    Dependency(name='pip', installer=CONDA),  # Without this Conda complains
    Dependency(name='coverage', version='==5.3', installer=CONDA, desc='test coverage'),  # DEV
    Dependency(name='pipdeptree', scope=DEV, installer=PIP),
    Dependency(name='coverage-badge'),  # default to DEV and PIP automatically.
    Dependency(name='twine'),  # uploading to pypi
    Dependency(name='conda-build', installer=CONDA),
    Dependency(name='conda-verify', installer=CONDA),
    Dependency(name='anaconda-client', installer=CONDA),
]

# ##############################################################################
# No need to change below, unless you want to customize
# ##############################################################################

install_required = pip_translator.get_install_required(dependent_libs)

test_required = pip_translator.get_test_required(dependent_libs)

python_required = pip_translator.get_python_requires(dependent_libs)

# we can't abstract this out since it knows pip and conda, maybe more later on.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError('need to pass in parameters: pip, conda, conda_env')

    if sys.argv[1] == 'pip':
        pip_translator.gen_req_txt(dependent_libs, 'requirements.txt')
    elif sys.argv[1] == 'conda':
        conda_translator.gen_conda_yaml(dependent_libs, 'environment.yml')
    elif sys.argv[1] == 'conda_env':
        print(CONDA.env)
    else:
        raise ValueError(f'unknown parameter {sys.argv[1]}')
