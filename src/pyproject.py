#!/usr/bin/env python3

#enconding=utf-8


#create a structure of project basic of python

#.
#├── .git
#├── LICENSE.md
#└── src
#    ├── __init__.py
#    └── pyproject.py

import os

DIRECTORY = "src"
PATH_DIRECTORY = os.path.join("./", DIRECTORY)

def exec_cmd():
    cmds = [
            "ignore python",
            'license-generator install mit -e md -y 2022 -n "Xizuth"'
            ]

    
    for cmd in cmds:
        os.system(cmd)

def create_files(name="main.py"):
    files = [name,"__init__.py","main.py"]
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

def main():
    create_src_folder()
    create_files()
    exec_cmd()


if __name__ == "__main__":
    main()
