#!/usr/bin/env python3

#enconding=utf-8


#create a structure of project basic of python

#.
#├── .git
#├── LICENSE.md
#└── src
#    ├── __init__.py
#    ├── __main__.py
#    └── my_project.py

import os
import sys
from datetime import datetime
from sys import argv, exit

DIRECTORY = "src"
PATH_DIRECTORY = os.path.join("./", DIRECTORY)

HELP = """
USAGE:
    pyproject [name_project]
    
    example:
        pyproject my_project

    
    https://github.com/jalmx/Pyproject
"""


def exec_cmd():
    cmds = [
            "ignore python",
            f'license-generator install mit -e md -y {datetime.now().year} -n "Xizuth"'
            ]

    
    for cmd in cmds:
        os.system(cmd)

def create_files(name="main.py"):
    files = [name,"__init__.py","__main__.py"]
    for file in files:
        open(os.path.join(PATH_DIRECTORY,file), "w")

    files = ["Readme.md"]
    
    for file in files:
        open(file, "w")
    

def create_src_folder():
    try:
        os.mkdir(PATH_DIRECTORY) 
        return True
    except: 
        return False

def pyproject(name):
    create_src_folder()
    name = name.replace(".py","")
    create_files(f"{name}.py")
    exec_cmd()


def cli():
    if len(argv) < 2:
        print(HELP)
        exit(1)

    name = argv[1]
    
    if name == "--help":
        print(HELP)
        exit(0)
    
    try:
        pyproject(name or "main.py")
    except Exception as e:
        print(e)
        print(HELP)
        exit(1)
    
    exit(0)

def main():
    cli()
    
if __name__ == "__main__":
    main()
