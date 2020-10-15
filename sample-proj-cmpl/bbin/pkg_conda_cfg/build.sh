#!/bin/bash

ls -ltr
ls -ltr $SRC_DIR
ls -ltr $PREFIX
ls -ltr $SCRIPTS

REM Or use %PREFIX%\Scripts
cp -R $SRC_DIR\bin $SCRIPTS
cp -R $SRC_DIR\conf $SCRIPTS
cp -R $SRC_DIR\dist $SCRIPTS
