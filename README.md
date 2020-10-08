### Python Project Setup Template

![Python Package using Conda](https://github.com/psilons/pypigeonhole-simple-utils/workflows/Python%20Package%20using%20Conda/badge.svg)
![Test Coverage](coverage.svg)

This is a project template for Python, and a workflow for GitHub to run 
CI (Continuous Integration) using Conda.

#### Here are the reasons why we create this template:

- Python, by nature, could have some C/C++ library dependencies, such as numpy, 
  PyQt, etc. These C/C++ libs sometimes require compilation (and thus a 
  compiler). This creates headaches in the past, very painful. Anaconda comes
  with pre-compiled packages and gets rid of these headaches for most commonly
  used libraries. So we use Anaconda packages whenever possible here. If 
  Anaconda does not have a package, then we fall back to pip. 
  >This does not mean that C/C++ is a drag for Python. In fact, this is a 
  strength Python has. If we need something faster than Python can do, do it 
  in C++ and wrap it.
- Dependent libraries are stored in setup.py, or requirements.txt for PIP, or 
  Anaconda's environment.yaml. Besides version information, we need to know
  whether a library is a real dependency or just needed for dev/testing. 
  setup.py has install_requires and test_require, but environment.yaml and 
  requirements.txt miss it. So we need to fill the gap here. This is done 
  by the underlying library, pypigeonhole-build. Furthermore, we only need to
  specify dependencies once(in dep_setup.py), not in several locations.
- We separate source files and test files into 2 folders next to each other,
  rather than one inside another. It's just cleaner. We make sure this setup
  works well with IDE setup and unit tests (don't count test file in coverage).
- Since half of the reusable code is in scripts, a template folder makes more
  sense than a library.
  
#### Here are the improvements:

- .github/workflows/python-package-conda.yaml: Most of the content comes from
  GitHub's action template (Python Package using Conda from Actions tab on the
  front page of a repo). It takes Conda's environment.yaml file to create Conda
  environment, run flake8 and unit tests. So this is a good CI setup. However,
  after the conda environment is set up, the Python executable is still pointing
  to the system wide Python executable. So we have to find a way around until 
  this is fixed. We also add the test coverage badge.
- dbin (dev bin) folder has the scripts needed to perform routine dev tasks, 
  such as project setup, unit tests, clean up & build. Furthermore, we add a
  packaging script for application packaging. setup.py is a library packager, 
  we need a packager for applications as well.
- IDE folder has IntelliJ setup, it needs the Python plugin. You may switch
  to Pycharm with your own setup. With this setup, the unit testing is very
  convenient.
- src/test names are borrow from Java Maven. Just labels. If you change them,
  then you have to go through all the code here to make additional changes.
  In order to run test at the project root folder, we add a src reference in
  the __init__.py under test top package. Otherwise, tests can run only from
  the src folder.
- dep_setup.py is where we specify dependencies with complete information, such
  as name, version, scope, installer(PIP or Conda), etc. setup.py has hooks in 
  dependency required sections. No dependency changes will touch this file.
  Check pypigeonhole-build docs for more details.
- environment.yaml is generated from py_dev_env_setup script. This is used by CI. So
  we have to run the script once and check in to GIT. Whenever we change 
  dependencies, we need to run the script and check it in.
  
#### Here are the suggestions:
** *nix shell scripts are not fully tested! **

For development:

All scripts in dbin, bbin and .github are reusable, unlikely need to change
along with projects. dep_setup.py controls dependencies and version.

- pip install ```pip install pypigeonhole-build```
- Add dependencies and set version in dep_setup.py. This is the main driver.
- run dbin/py_dev_env_setup, it does the following:
    - create Conda environment.yaml, need to check this for CI
    - run Conda to create virtual environment, activate, and print out the
      dependency tree. Whenever there is a change in dep_setup.py, rerun
      this step.
- work on development and unit testing. 
- Once we finish development, run dbin\unittest

That's it, the reusable code minimizes the necessary work for dependency 
management and CI. 

For release:

Standard SDLC steps are:

- Compile: such as no compile, C/C++ compile and wrapping, PyInstaller, 
  Cython, etc. A lot of variations here.
- package: setup.py is a library packager. We create an application packager
  in bbin(build bin) as an extra way to pack. It creates a zip file from
  certain folders, bin, conf, src or output from builds.
- release: tag version in GIT. It's manual now (web interface).
- upload: such as PyPI, Artifactory, Nexus, etc. A lot of variations here.
- deploy: such as manual kubernetes, Ansible, etc. A lot of variations here.

So we tackle the reusable steps, application packaging and release, other 
steps vary quite a bit. In our case, upload is simple too.

|         | library   | application  |
|---------|-----------|--------------|
| compile | separate  | separate     |
| package | setup.py  | *pack_app*   |
| release | *release* | *release*    |
| upload  | *upload*  | upload       |
| deploy  | N/A       | deploy       |


#### Side Notes 

- During CI, we check the svg file back to GIT, so that the above percentage
  shows up. This requires every checkin to re-pull. 
