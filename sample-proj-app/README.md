This is a sample for pypigeonhole-build to build a reusable lib.

## Python Environment Setup

Install miniconda, if needed, from https://docs.conda.io/en/latest/miniconda.html

We need to install this package in order to use its scripts.

```conda install -c psilons pypigeonhole-build```

Use IntelliJ or other IDEs to create a project in the folder sample-proj-app
Under there, create the following:

- src folder: for python code
- create top package under src, it should be the project folder name 
  with _ instead of - . In this case, it's sample_proj_app.
- test folder: for python test code
- create top package under test, it should be ```test_<top package in src>```.
  In this case, it's test_sample_proj_app
- a blank README.md file that we could fill in later.
- setup.py: copy from pypigeonhole-build\src\pypigeonhole_build\dep_setup.py 
  to the top package in src, we will modify it later.
- app_setup.py: copy from pypigeonhole-build\src\pypigeonhole_build\app_setup.py 
  to the top package in src, we will modify it later.
- ```__init__.py```: copy from pypigeonhole-build\test\pypigeonhole_build\.
  Notice that there is some hook code in this file for unit testing. No need
  to change it.
  
Now follow these steps:
- change __app_version to 0.1.0 in app_setup.py
- add 2 dependencies to dependent_libs in dep_setup.py:  
    ```Dependency(name='psutil', scope=INSTALL),```     
    ```Dependency(name='pypigeonhole-build', installer=CONDA),```
- add psilons to the channels in dep_setup.py 
- setup.py: modify the import statement to point to sample_proj_app.

Now let's open a command window, and go to the project folder. Run 

```pph_dev_env_setup 2>&1 | tee a.log```

to create the conda environment with the name ```py390_sample_proj_app``` 
specified in the dep_setup.py.

This step also creates requirements.txt and environment.yml. After it's down,
run ```conda info --envs``` to check the new environment is in the right path.
Run ```conda activate py390_sample_proj_app```

If needed, run ```conda clean -a``` to clear conda cache (from time to time).

## Coding and Testing
Back to IDE and change the setting to use this new environment.

Let's create some sample code, create sample_feature.py under the top package 
and fill in some python logic. Since this is an app, we create a main method
in the file.

In the test folder, write some test case. Make sure it works in the IDE, and
it gets proper test coverage. 
Run ```pph_unittest```, this generates .coverage and a badge coverage.svg.

In the project folder, ```pip install -e .``` creates a soft link in the
python environment, if needed during cross development.


## Package

If all goes well, it's time to package our code and ship it out. Run 

```pph_package_pip 2>&1 | tee b.log```

This generates a few things:
- sample_proj_app.egg-info under src, this is package info.
- build folder under project, this is intermediate staging folder.
- dist folder under project, there are 2 artifacts in this folder.

In order to build conda package, we need to follow conda-build convention.
Let's create a bbin (build bin) folder under project, then a pkg_conda_cfg
folder under bbin. This path is hard-coded in the following script. There
are 3 files here, meta.yaml, bld.bat, and build.sh. conda-build calls these
files. Please read conda-build docs for more details.

This is an app with a bin\run_this.bat file and a conf\settings.txt, we 
need to copy these files to the %SCRIPTS% folder in the 
bbin\pkg_conda_cfg\bld.bat .

Now run 

```pph_package_conda 2>&1 | tee c.log```

It generates output in dist_conda folder under project. We care the file 
dist_conda\noarch\sample-proj-app-0.1.0-pyt_0.tar.bz2

Make sure conda is clean after build. conda-build corrupts conda environments,
and so run it outside.

```conda info --envs```


## Local Testing   

To test pip package:
- pip uninstall sample-proj-app -y
- pip install dist\sample-proj-app-0.1.0.tar.gz
- python -c "import sample_proj_app.dep_setup as ds; print(ds.app_version)"
- check ```<env>\Lib\site-packages\sample_proj_app``` for files
- pip uninstall sample-proj-app -y
- pip install dist\sample_proj_app-0.1.0-py3-none-any.whl
- python -c "import sample_proj_app.dep_setup as ds; print(ds.app_version)"
- check ```<env>\Lib\site-packages\sample_proj_app``` for files
- pip uninstall sample-proj-app -y

To test conda package:
- conda remove sample-proj-app -y
- conda install dist_conda\noarch\sample-proj-app-0.1.0-py_0.tar.bz2
- python -c "import sample_proj_app.dep_setup as ds; print(ds.app_version)"
- check ```<env>\Lib\site-packages\sample_proj_app``` for files
- ```<Anaconda root>\envs\py390_sample_proj_app\Scripts\run_this.bat```
- conda remove sample-proj-app -y


## Upload and Testing   

```pph_upload_pip```

```pph_upload_pip_test```

```pph_upload_conda dist_conda\noarch\sample-proj-app-0.1.0-py_0.tar.bz2```

To test: same process as before, except we install from central server:

```pip install sample-proj-app``` and ```conda install -c psilons sample-proj-app```

We may add the channel psilons to the config:

```conda config --add channels psilons```

To check whether it's in the config:

```conda config --get channels```


## Release and Cleanup

Now check all changes, and run

```pph_release```

Finally, we clean up all the generated files.

```pph_cleanup```

Try to commit again, there should be nothing to commit.

```conda deactivate```
