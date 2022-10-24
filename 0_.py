# ...! cd d:\mysenv\scripts\ .\activate.ps1
"""Task-1

c:\Python39\python.exe -m pip install build
cd D:\projects\Denys-hw-73\clean_folder_tdv1
c:\Python39\python.exe -m build

python -m venv /path/to/new/virtual/environment
C:\p\Scripts\python.exe -m build

D:\mysenv\Scripts\python.exe -m build

D:\projects\myenv\Scripts\python.exe -m pip install build

D:\projects\myenv\Scripts\python.exe -m build

python3 -m pip list
or
pip list

python3 -m venv /path/to/new/virtual/environment

\path\to\new\virtual\environment\Scripts\activate.bat або 
source /path/to/new/virtual/environment/bin/activate # для Linux / Mac OS. 
Якщо ви використовуєте PowerShell, то можна виконати: 
\path\to\new\virtual\environment\Scripts\Activate.ps1.

cd d:\mysenv\scripts
./activate

!!! Its only for example!
"""

import os
import sys
import pickle


def func_init_1():
    pass


def main():
    func_init_1()


if __name__ == "__main__":
    main()

# print(1.001**sys.float_info.max)
# print(sys.int_info)
# print(type(sys.maxsize))


def input_error(handler):
    def excp_fun():
        pass
        result = handler()
        pass
        return result
    return excp_fun

# @input_error
# def handler
# ....
