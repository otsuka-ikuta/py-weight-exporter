#!/bin/bash -u

# cd $projectHome
# source venv/activate
pyinstaller -F -c py-weight-exporter.py
cp dist/py-weight-exporter ~/bin/
