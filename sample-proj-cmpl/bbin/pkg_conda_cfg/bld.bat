echo %cd%

ls -ltr
ls -ltr %SRC_DIR%
ls -ltr "%SCRIPTS%"

mkdir "%SCRIPTS%"
ls -ltr %PREFIX%

REM don't work on directories, not working. Use existing directories.

xcopy %SRC_DIR%\bin "%SCRIPTS%"
xcopy %SRC_DIR%\conf "%SCRIPTS%"
xcopy %SRC_DIR%\dist "%SCRIPTS%"
