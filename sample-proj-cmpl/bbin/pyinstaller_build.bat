SET script_dir=%~dp0

SET proj_dir=%script_dir%..

REM dist and build folders are default outputs in pyinstaller, we just illustrate overwrite
REM conda or zip will pick up from dist later.
rmdir /Q /S %proj_dir%\build
rmdir /Q /S %proj_dir%\dist

pyinstaller --onefile --name my_app --noupx --icon %script_dir%app.ico^
    --paths=%proj_dir%\src\sample_proj_cmpl^
    --distpath %proj_dir%\dist --workpath %proj_dir%\build^
    %proj_dir%\src\sample_proj_cmpl\my_app.py


