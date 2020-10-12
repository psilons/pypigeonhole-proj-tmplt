SET ProjDir=%~dp0
IF NOT EXIST setup.py (
    ECHO Please go to project folder!
    EXIT /B 1
)
echo Project Folder: %ProjDir%

REM conda flattens the folder structure so this file and settings.txt are in same folder.
python -m sample_proj_app.sample_feature %ProjDir%
