echo %cd%

ls -ltr
ls -ltr %SRC_DIR%
ls -ltr %PREFIX%

echo copying scripts to %PREFIX%...
xcopy %SRC_DIR%\bin "%PREFIX%"
xcopy %SRC_DIR%\conf "%PREFIX%"

ls -ltr %PREFIX%

%PYTHON% -m pip install .
