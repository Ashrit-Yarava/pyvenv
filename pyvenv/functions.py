import os, shutil, subprocess, venv, clipboard
from pathlib import Path
from termcolor import cprint

def create(environment_name):
    """
    Create a new environment with the given name.
    """
    path = Path.home() / Path('.local/share/pyvenv')
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    path = path / Path(environment_name)
    if path.exists():
        cprint(f'Environment already exists!\nRun: pyvenv remove {environment_name}', "red")
        exit(1)
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
    current_shell = Path(os.environ['SHELL']).parts[-1]
    path = Path.home() / Path('.local/share/pyvenv') / Path(environment_name)
    command = ""

    if not path.exists():
        cprint(f"{environment_name} does not exist.", 'red')
        exit(1)

    if current_shell == 'bash' or current_shell == 'zsh':
        command = f"source {path / Path('bin/') / Path('activate')}"
    
    elif current_shell == 'fish':
        command = f". {path / Path('bin/') / Path('activate.fish')}"

    elif current_shell == 'csh' or current_shell == 'tcsh':
        command = f"source {path / Path('bin/') / Path('activate.csh')}"

    elif current_shell == 'cmd.exe':
        command = f"{path / Path('Scripts/') / Path('Activate.bat')}"

    elif current_shell == 'powershell.exe':
        command = f"{path / Path('Scripts/') / Path('Activate.ps1')}"

    else:
        cprint(f"Unknown shell: {current_shell}", "red")
        cprint(f"Environment located at: {path}", "green")
        exit(1)

    clipboard.copy(command)
    cprint(f"Copied {command} to clipboard.", "green")