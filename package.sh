#!/bin/sh
set -x

rm package.zip

set -eux pipefail

pip install -t lib -r requirements.txt
(cd lib; zip ../package.zip -r .)
(cd app; zip ../package.zip -u main.py)

rm -rf lib