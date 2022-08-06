#!/bin/sh

# pip install python-minifier # if failed install this
NAME_SCRIPT="pyproject"

rm -rf bin

mkdir -p bin

pyminify ./src/$NAME_SCRIPT.py --output ./bin/$NAME_SCRIPT
sudo chmod +x bin/$NAME_SCRIPT