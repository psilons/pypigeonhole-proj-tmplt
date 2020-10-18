#!/bin/bash

ls -ltr
ls -ltr $SRC_DIR
ls -ltr $PREFIX

echo copying scripts to %PREFIX%...
cp -R $SRC_DIR/bin/* $PREFIX
cp -R $SRC_DIR/conf/* $PREFIX
cp -R $SRC_DIR/dist/* $PREFIX
