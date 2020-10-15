from setuptools import setup, find_packages
import pathlib
import sys
import os.path
from os.path import dirname

# To add source folder to the path, otherwise below import would fail.
src_path = os.path.join(dirname(__file__), 'src')
sys.path.append(src_path)

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from sample_proj_cmpl import app_setup
from sample_proj_cmpl import dep_setup

# If this is needed during dev by others, cd this folder and run pip install -e .
# This is reusable in normal cases.
setup(name=app_setup.get_app_name(),  # 'sample-proj-app',
      version=app_setup.get_app_version(),  # major.minor.patch
      description='Python build sample project for libs',
      url='https://github.com/psilons/pypigeonhole-proj-tmplt.git',

      author='psilons',
      author_email='psilons.quanta@gmail.com',

      long_description=README,
      long_description_content_type="text/markdown",
      license="MIT",

      package_dir={'': 'src'},
      packages=find_packages("src", exclude=["test"]),

      python_requires=dep_setup.python_required if dep_setup.python_required else '>=3',

      install_requires=dep_setup.install_required,

      tests_require=dep_setup.test_required,

      extras_require={},
      )
