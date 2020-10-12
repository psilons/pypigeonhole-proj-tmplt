### Python Project Setup Template

![Python Package using Conda](https://github.com/psilons/pypigeonhole-simple-utils/workflows/Python%20Package%20using%20Conda/badge.svg)
![Test Coverage](coverage.svg)

This is a project template for Python, and a workflow for GitHub to run 
CI (Continuous Integration) using Conda.

  
#### Here are the improvements:

- .github/workflows/python-package-conda.yaml: Most of the content comes from
  GitHub's action template (Python Package using Conda from Actions tab on the
  front page of a repo). It takes Conda's environment.yaml file to create Conda
  environment, run flake8 and unit tests. So this is a good CI setup. However,
  after the conda environment is set up, the Python executable is still pointing
  to the system wide Python executable. So we have to find a way around until 
  this is fixed. We also add the test coverage badge.



|         | library   | application  |
|---------|-----------|--------------|
| compile | separate  | separate     |
| package | setup.py  | *pack_app*   |
| release | *release* | *release*    |
| upload  | *upload*  | upload       |
| deploy  | N/A       | deploy       |


