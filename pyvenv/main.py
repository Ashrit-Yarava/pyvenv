from pyvenv.utils import parse_args
from pyvenv.functions import create, remove, shell
from termcolor import cprint

def main():
    option, value = parse_args()

    if option[0] == 'create':
        create(option[1])
    elif option[0] == 'remove':
        remove(option[1])
    elif option[0] == 'shell':
        shell(option[1])
    else:
        cprint(f"Something went wrong...", "red")