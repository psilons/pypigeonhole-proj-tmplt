#!/bin/bash

ls -ltr
ls -ltr %SRC_DIR%
ls -ltr %PREFIX%

echo copying scripts to $PREFIX ...
cp -R $SRC_DIR/dbin/* $PREFIX
cp -R $SRC_DIR/bbin/* $PREFIX

ls -ltr $PREFIX

$PYTHON -m pip install . --no-deps --ignore-installed -vv
