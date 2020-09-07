import os, shutil, subprocess
from pathlib import Path
from termcolor import cprint
from venv import create
from clipboard import copy

def create(environment_name):
    """
    Create a new environment with the given name.
    """
    path = Path.home() / Path('.local/share/pyvenv')
    path.makedirs()
    path = path / Path(environment_name)
    if path.exists():
        cprint(f'Environment already exists!\nRun: pyvenv remove {environment_name}', "red")
    else:
        venv.create(path, with_pip=True)
    

def remove(environment_name):
    """
    Remove an existing environment with the given name.
    """
    path = Path.home() / Path('.local/share/pyvenv') / Path(environment_name)
    try:
        shutil.rmtree(path)
    except:
        cprint(f'Error deleting directory: {path}', "red")


def shell(environment_name):
    """
    Activate a shell environment.
    """
    current_shell = os.environ['SHELL']
    path = Path.home() / Path('.local/share/pyvenv') / Path(environment_name)
    command = ""

    if not path.exists():
        cprint(f"{environment_name} does not exist.", 'red')

    if current_shell == 'bash' or current_shell == 'zsh':
        command = f"source {path / Path('bin/')}activate"
    
    elif current_shell == 'fish':
        command = f". {path / Path('bin/')}activate.fish"

    elif current_shell == 'csh' or current_shell == 'tcsh':
        command = f"source {path / Path("bin/")}activate.csh"

    elif current_shell == 'cmd.exe':
        command = f"{path / Path("Scripts/")}Activate.bat"

    elif current_shell == 'powershell.exe':
        command = f"{path / Path("Scripts/")}Activate.ps1"

    else:
        cprint(f"Unknown shell: {current_shell}", "red")
        cprint(f"Environment located at: {path}", "green")
        exit(0)

    clipboard.copy(command)
    cprint(f"Copied {command} to clipboard.")