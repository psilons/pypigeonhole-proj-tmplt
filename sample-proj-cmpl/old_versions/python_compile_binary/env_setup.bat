conda update -n base -c defaults conda

python -m pip install --upgrade pip

conda create --name py385_cb python=3.8.5

conda activate py385_cb

conda env update -n py385_cb -f env_conda.yaml

REM collect all (transitive) dependent libs
REM pip freeze > requirements.txt

REM This collects all (transitive) dependent libs as well
REM conda list -e
REM conda env export > env_conda_all.yaml

REM collect only top level dependent libs
pipdeptree | grep -e "^[^ ]" > requirements.txt
