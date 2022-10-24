import os


def which(pgm):

    path = os.getenv('PATH')
    for p in path.split(os.path.pathsep):
        p = os.path.join(p, pgm)
        if os.path.exists(p) and os.access(p, os.X_OK):

            return p


print(which("python.exe"))


"""
cd d:\mysenv\scripts
./activate

Run in powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
> -Scope CurrentUse
"""
