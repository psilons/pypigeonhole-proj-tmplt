# Compile Python with PyInstaller

Compile Python code to an executable, then wrap scripts, configuration, 
and the executable in a conda or zip file. The conda package can then be
uploaded to the server, then installed to needed environment.

## PyInstaller Compiling

Run ```bbin\pyinstaller_build.bat```, the executable is in the dist folder.

Please see PyInstaller document for details.

## Conda Packaging
Create the conda configuration in bbin\pkg_conda_cfg. There is one step out of
ordinary - need to create the Scripts folder for copying (The ordinary case is
that the folder is already there).

Run ```pph_package_conda.bat```, the output is in the dist_conda\win-64 folder.
The .bz2 file contains bin\my_app_start.bat, conf\my_app_setting.tx, and 
dist\my_app.exe in the Scripts folder. These files will be copied to the
Scripts folder in the target environment. It would be better to keep the same
prefix for all files in order to group them together.

There is a catch when we test this .bz2 file locally, through installation:

```conda install dist\win-64\sample-proj-cmpl-0.1.1-0.tar.bz2```

After the initial installation, Conda caches this file. Run
```conda info``` to find out where the cache location. Delete the cached 
before installing it again.

## Zip 

Run ```pph_pack_app_zip.bat```, the output is in dist_zip. By default, it
zips bin, conf, and dist folders.


## License

Free Fire icon is from https://www.flaticon.com/free-icon/fire_1843793
