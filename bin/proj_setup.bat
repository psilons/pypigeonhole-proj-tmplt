SET WorkDir=%cd%
SET BatchDir=%~dp0

cd %BatchDir%..
if not exist dep_setup.py (
    echo Please create dep_setup.py in project root first!
    cd %WorkDir%
    exit 1
)

python dep_setup.py
REM environment.yaml should be created for conda installation

conda env create -f environment.yaml

FOR /F %%I IN ('python dep_setup.py env') DO SET env_name=%%I
conda activate %env_name%

REM print dependency tree
pipdeptree

cd %WorkDir%
