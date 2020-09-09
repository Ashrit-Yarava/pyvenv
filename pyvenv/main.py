from pyvenv.utils import parse_args
from pyvenv.functions import create, remove, shell, listShells
from termcolor import cprint

def main():
    option, value = parse_args()

    if option == 'create':
        create(value)
    elif option == 'remove':
        remove(value)
    elif option == 'shell':
        shell(value)
    elif option == 'list':
        listShells()
    else:
        cprint(f"Something went wrong...", "red")