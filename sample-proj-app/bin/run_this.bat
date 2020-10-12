SET ProjDir=%~dp0
IF NOT EXIST setup.py (
    ECHO Please go to project folder!
    EXIT /B 1
)
echo Project Folder: %ProjDir%

python -m sample_proj_app.sample_feature %ProjDir%
