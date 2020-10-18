This is a sample for pypigeonhole-build to build an application with PyInstaller.

# Python Project Setup

Install miniconda, if needed, from https://docs.conda.io/en/latest/miniconda.html

Install this package to the base env in order to use its scripts to create
other environments

```conda install -c psilons pypigeonhole-build```

Use IntelliJ or other IDEs to create a project in the folder sample-proj-cmpl
Under there, create the following:

- src folder: for python code
- create top package under src, it should be the project folder name 
  with _ instead of - . In this case, it's sample_proj_cmpl.
- test folder: for python test code
- create top package under test, it should be ```test_<top package in src>```.
  In this case, it's test_sample_proj_cmpl.
- a blank README.md file that we could fill in later.
- setup.py: copy from pypigeonhole-build\src\pypigeonhole_build\dep_setup.py 
  to the top package in src, we will modify it later.
- app_setup.py: copy from pypigeonhole-build\src\pypigeonhole_build\app_setup.py 
  to the top package in src, we will modify it later.
- dep_setup.py: copy from pypigeonhole-build\src\pypigeonhole_build\dep_setup.py 
  to the top package in src, we will modify it later.
- ```__init__.py```: copy from pypigeonhole-build\test\pypigeonhole_build\.
  Notice that there is some hook code in this file for unit testing. No need
  to change it.
  
Now follow these steps:
- change __app_version to 0.1.0 in app_setup.py
- add 2 dependencies to dependent_libs in dep_setup.py:  
    ```Dependency(name='psutil', scope=INSTALL),```  
    ```Dependency(name='pyinstaller', installer=CONDA),```   
    ```Dependency(name='pypigeonhole-build', installer=CONDA),```
- add psilons to the channels in dep_setup.py 
- setup.py: modify the import statement to point to sample_proj_cmpl.


## Conda Environment Setup

The interface script ```pphsdlc.sh``` or ```pphsdlc.bat``` has the
following options (run the script without parameter):

  - setup: create conda environment specified in dep_setup.py
  - test: run unit tests and collect coverage
  - package: package artifact with pip | conda | zip
  - upload: upload to pip | piptest | conda
  - release: tag the current version in git and then bump the version
  - cleanup: cleanup intermediate results in filesystem
  - help or without parameter: this menu
  
Now let's open a command window, and go to the project folder. Run 

```pphsdlc setup 2>&1 | tee a.log```

to create the conda environment with the name ```py390_sample_proj_cmpl``` 
specified in the dep_setup.py.

This step also creates requirements.txt and environment.yml. After it's down,
run ```conda info --envs``` to check the new environment is in the right path.
Run ```conda activate py390_sample_proj_cmpl```

If needed, run ```conda clean -a``` to clear conda cache (from time to time).


## Coding and Testing
Back to IDE and change the setting to use this new environment.

Let's create some sample code, create sample_feature.py under the top package 
and fill in some python logic. Since this is an app, we create a main method
in the file.

In the test folder, write some test case. Make sure it works in the IDE, and
it gets proper test coverage. 
Run ```pphsdlc test```, this generates .coverage and a badge coverage.svg.

In the project folder, ```pip install -e .``` creates a soft link in the
python environment, if needed during cross development. Otherwise, skip this
step.


## Package

In this case, we skip the pip package step and use PyInstaller as a packager.

Check bbin folder for PyInstaller related files. Please see PyInstaller 
document for details. Run 

```bbin\pyinstaller_build.bat```

The executable is in the dist folder. Run ```my_app.exe conf``` to see the 
prints.

Now we use conda to pack the executable, bin\my_app_start.bat, and 
conf\my_app_settings.txt(The prefix my_app* group all relevant files 
together in the <env> folder later). Check bbin\pkg_confa_cfg for conda-build
related files, we copy above files to the target folder. Run

```pphsdlc package conda 2>&1 | tee b.log```

The output is in dist_conda\win-64 folder(This is OS dependent).

Now if we are on windows and run 
```conda info --envs``` or ```conda env list```, 
we may see that conda environments are mislabeled now. If this is the case,
close this window and open a new window. Activate the environment again.
It seems that in this case, we are good(We don't have python -m pip install
in bld.bat in this case).

Alternatively, there is a zip package as well in case you want to handle
packaging + transport by your own.

```pphsdlc package zip```

The output is in dist_zip. 
By default, it zips bin, conf, and dist folders.
tar + zip is across OS platforms and compact.

## Local Testing  

Version may vary, so don't blindly copy-paste:
- conda remove sample-proj-cmpl -y
- conda install dist_conda\win-64\sample-proj-cmpl-0.1.1-0.tar.bz2
- run ```my_app_start.bat```, this is installed in the env and the env path
  is already on your path(This is where python is).

There is a catch when we test this .bz2 file locally, through installation:

```conda install dist\win-64\sample-proj-cmpl-0.1.1-0.tar.bz2```

After the initial installation, Conda caches this file. Run
```conda info``` to find out where the cache location. Delete the cached 
zip files and folders before installing it again. It would be better to 
bump the version.
conda clean --all --force-pkgs-dirs is a little too much.


## License

Free Fire icon is from https://www.flaticon.com/free-icon/fire_1843793
