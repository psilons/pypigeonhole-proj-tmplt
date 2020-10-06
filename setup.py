from setuptools import setup, find_packages

import dep_setup

# If this is needed during dev by others, cd this folder and run pip install -e .
setup(name='your fancy name here',
      version='0.1.0',  # major.minor.patch
      description='your description here',
      url='repo url for source code',

      author='nice name',
      author_email='your email here',

      package_dir={'': 'src'},
      packages=find_packages("src", exclude=["test"]),

      python_requires='>=3',

      install_requires=dep_setup.install_required,

      tests_require=dep_setup.test_required,

      extras_require={},
      )
