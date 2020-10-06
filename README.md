### Python Project Setup Template

![Python Package using Conda](https://github.com/psilons/pypigeonhole-simple-utils/workflows/Python%20Package%20using%20Conda/badge.svg)
![Test Coverage](coverage.svg)

This is a project template for Python, and a workflow for GitHub to run 
CI (Continuous Integration) using Conda.

##### Here are the reasons why we create this template:

- Python, by nature, could have some C/C++ library dependencies, such as numpy, 
  PyQt, etc. These C/C++ libs sometimes require compilation (and thus a 
  compiler). This creates headaches in the past, very painful. Anaconda comes
  with pre-compiled packages and gets rid of these headaches for most commonly
  used libraries.So we use Anaconda packages whenever possible here. If 
  Anaconda does not have a package, then we fall back to pip. This does not 
  mean that C/C++ is a drag for Python. In fact, this is a strength Python has. 
  If we need something faster than Python can do, do it in C++ and wrap it.
- Dependent libraries are stored in setup.py, or requirements.txt for PIP, or 
  Anaconda's environment.yaml. Besides version information, we need to know
  whether a library is a real dependency or just needed for dev/testing. 
  setup.py has install_requires and test_require, but Anaconda misses it. So
  we need to fill the gap here. We view our fix as a temporary patch until
  Python.org and Anaconda come up with a solid solution. We separate the 
  development concerns from the runtime dependencies with scopes (borrowed
  from Java Maven). This is the missing information. However, the hook from 
  user side is a bit tedious - we can't do it in one shot, but two. Once the 
  hook is buried at the lower level, users should have a pleasant trip - they 
  only need to specify dependencies and run the environment setup. That's all.
  This is what we have in Java now.
- We separate source files and test files into 2 folders next to each other,
  rather than one inside another. It's just cleaner. We make sure this setup
  works well with IDE setup and unit tests (don't count test file in coverage).
- Since half of the reusable code is in scripts, a template folder makes more
  sense than a library.
  
##### Here are the improvements:

- .github/workflows/python-package-conda.yaml: Most of the content comes from
  GitHub's action template (Python Package using Conda from Actions tab on the
  front page of a repo). It takes Conda's environment.yaml file to create Conda
  environment, run flake8 and unit tests. So this is a good CI setup. However,
  after the conda environment is set up, the Python executable is still pointing
  to the system wide Python executable. So we have to find a way around until 
  this is fixed. We also add the test coverage badge (borrowed from the 
  internet and modify a bit)
- bin folder has the scripts needed to perform routine dev tasks, such as
  project setup, unit tests, clean up & build. The Python script here should be
  moved to the lower level with modification. It's the clue code used by 
  dep_setup.py.
- IDE folder has IntelliJ setup, it needs the Python plugin. You may switch
  to Pycharm with your own setup. With this setup, the unit testing is very
  convenient.
- src/test names are borrow from Java Maven. Just labels. If you change them,
  then you have to go through all the code here to make additional changes.
  In order to run test at the project root folder, we add a src reference in
  the __init__.py under test top package. Otherwise, tests can run only from
  the src folder.
- dep_setup.py is where we specify dependencies with complete information, such
  as name, version, scope, installer(PIP or Conda), etc. Here we take a 
  shortcut, mixing PIP and Conda. These should be separated in the future.
- environment.yaml is generated from proj_setup script. This is used by CI. So
  we have to run the script once and check in to GIT. Whenever we change 
  dependencies, we need to run the script and check it in.
- setup.py has the hook in required sections. No dependency changes will touch
  this file.
  
##### Here are the suggestions:
- Add dependencies in dep_setup.py. This is the main driver.
- run bin/project_setup, it does the following:
    - create Conda environment.yaml
    - run Conda to create virtual environment, activate, and print out the
      dependency tree.
- work on development and unit testing. 
- Include a dependency, pipdeptree, it prints the dependency tree.

That's it, dependencies takes the majority time during set up, and we do only 
minimal work. Then we could concentrate on the real development.
Once we check code in, CI kicks off automatically.

##### Side Notes 
- The unit test coverage is just for sample code, not for our glue code, 
  bin\dep_setup_utils.py. The testing for glue code is done by local and CI.
- During CI, we check the svg file back to GIT, so that the above percentage
  shows up. This requires every checkin to re-pull. This is a hack until GitHub
  has a better solution. (I can host a Jenkins for that too.)
