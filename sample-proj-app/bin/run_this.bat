SET ProjDir=%~dp0

REM conda flattens the folder structure so this file and settings.txt are in same folder.
python -m sample_proj_app.sample_feature %ProjDir%
