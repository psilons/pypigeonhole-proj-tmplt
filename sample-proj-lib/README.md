This is a sample for pypigeonhole-build to build a reusable lib.

## Python Environment Setup

Install miniconda, if needed, from https://docs.conda.io/en/latest/miniconda.html

We need to install this package in order to use its scripts.
conda install -c psilons pypigeonhole-build

Use IntelliJ or other IDE to create a project in the folder sample-proj-lib
Under there, create the following:

- src folder: for python code
- test folder: for python test code
- a blank README.md file that we could fill in later.
- setup.py: copy from pypigeonhole-build\setup.py, we will modify it later.

Now follow these steps:
- create the top python package sample_proj_lib (replace - with _ from project 
  name), this means we need a __init__.py file under this folder.
- dep_setup.py: copy from pypigeonhole-build\src\pypigeonhole_build\dep_setup.py.
  modify the content to reflect this project:
  
    - change app_version and CONDA.channels
    - add dependencies, psutil(for our feature) and pypigeonhole-build
    - others you may change

- setup.py: modify the import statement to point to sample_proj_lib (line 11).

Now let's open a command window, and go to the project folder. Or in an 
existing window, deactivate conda environment and then run 
```pph_dev_env_setup 2>&1 | tee a.log```, 
to create the conda environment with the name ```py390_sample_proj_lib``` 
specified in the dep_setup.py.

This step also creates requirements.txt and environment.yaml. After it's down,
we should be in the conda environment already. run ```conda info --envs``` to
check the new environment is in the right path.

If needed, run ```conda clean -a``` to clear conda cache.

## Coding and Testing
Back to IDE and change the setting to use this new environment.

Let's create some sample code, create sample_feature.py under the top package 
and fill in some python logic. 

In the test folder, write some test case. Make sure it works in the IDE, and
it gets proper test coverage. Now copy the top __init__.py from 
pypigeonhole-build\test\test_pypigeonhole_build to test\test_sample_proj_lib.
This adds the hook from test to src.
Now activate the new environment and run ```pph_unittest```, 
this generates .coverage and a badge coverage.svg.

In the project folder, ```pip install -e .``` creates a soft link in the
python environment, if needed.


## Package

If all goes well, it's time to package our code and ship it out. Run 
```pph_package_pip.bat 2>&1 | tee b.log```, this generates a few things:
- sample_proj_lib.egg-info under src, this is package info.
- build folder under project, this is intermediate staging folder.
- dist folder under project, there are 2 artifacts in this folder.

In order to build conda package, we need to follow conda-build convention.
Let's create a bbin (build bin) folder under project, then a pkg_conda_cfg
folder under bbin. This path is hard-coded in the following script. There
are 3 files here, meta.yaml, bld.bat, and build.sh. conda-build calls these
files. Please read conda-build docs for more details.

Since pypigeonhole-build is only in the channel psilons. We need to add this
channel to local config:
```conda config --add channels psilons```, to check the configuration, run
```conda config --get channels``` and psilons should show up in the list.

Now let's get out of the conda environment and run 
```pph_package_conda 2>&1 | tee c.log```, 
it generates output in dist_conda folder under project. We care the file 
dist_conda\noarch\sample-proj-lib-0.0.1-pyt_0.tar.bz2

Make sure conda is clean after build. conda-build corrupts conda environments,
and so run it outside.

```conda info --envs```


## Upload and Testing   

Let's use the same command window we opened during env setup. Make sure we are
in the project folder, and the conda env we created.

To test pip package:
- pip uninstall sample-proj-lib -y  
- pip install dist\sample-proj-lib-0.1.0.tar.gz  
- python -c "import sample_proj_lib.dep_setup as ds; print(ds.app_version)"
- check <env>\Lib\site-packages\pypigeonhole_build for 4 files
- pip uninstall sample-proj-lib -y
- pip install dist\sample_proj_lib-0.1.0-py3-none-any.whl
- python -c "import sample_proj_lib.dep_setup as ds; print(ds.app_version)"
- check <env>\Lib\site-packages\pypigeonhole_build for 4 files
- pip uninstall sample-proj-lib -y

To test conda package:
- conda remove sample-proj-lib -y
- conda install dist_conda\noarch\sample-proj-lib-0.1.0-py_0.tar.bz2
- python -c "import sample_proj_lib.dep_setup as ds; print(ds.app_version)"
- check <env>\Lib\site-packages\pypigeonhole_build for 4 files
- conda remove sample-proj-lib -y

## Upload

```pph_upload_pip```

```pph_upload_pip_test```

```pph_upload_conda dist_conda\noarch\pypigeonhole-build-0.2.4-py_0.tar.bz2```

## Release and Cleanup

```pph_release```

```pph_cleanup```
