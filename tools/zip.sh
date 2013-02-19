#!/bin/bash

cd $(dirname $0)/../dspl || exit
ZIPFILE=../dspl.zip

if [ -f $ZIPFILE ]; then rm $ZIPFILE; fi
zip $ZIPFILE *
