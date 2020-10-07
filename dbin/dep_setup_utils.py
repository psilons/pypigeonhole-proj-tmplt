from dataclasses import dataclass, field
import os


@dataclass
class Installer:
    name: str
    env: str = None
    channels: list = field(default_factory=list)


PIP = Installer(name='pip')
CONDA = Installer(name='conda')

INSTALL = 'install'
DEV = 'dev'


@dataclass
class Dependency:
    name: str
    version: str = ''
    url: str = None
    scope: str = DEV
    installer: Installer = PIP
    desc: str = None


def gen_conda_yaml(libs):  # output all libs, install or dev.
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(curr_dir, '../environment.yaml')
    with open(output_file, 'w') as f:
        f.write(f'name: {CONDA.env}\n')
        f.write('\n')

        f.write('channels:\n')
        for c in CONDA.channels:
            f.write(f'    - {c}\n')
        f.write('\n')

        f.write('dependencies:\n')
        # we do it this because we need to keep the order of the input.
        for lib in libs:
            if lib.installer == CONDA:
                f.write(f'    - {lib.name}{lib.version}\n')

        f.write('    - pip:\n')
        for lib in libs:
            if lib.installer == PIP:
                if lib.url:
                    f.write(f'        - {lib.url}')
                else:
                    f.write(f'        - {lib.name}{lib.version}\n')


def get_install_required(libs):
    return _find_dep_for_scope(libs, INSTALL)


def get_test_required(libs):
    return _find_dep_for_scope(libs, DEV)


def _find_dep_for_scope(libs, scope):
    ret = []
    for lib in libs:
        if lib.scope == scope:
            # https://stackoverflow.com/a/54794506/7898913
            if lib.url:
                ret.append(f'{lib.name} @ {lib.url}')
            else:
                ret.append(f'{lib.name}{lib.version}')
    print(f'test_required={ret}')
    return ret
