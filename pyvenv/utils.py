import os, sys


def print_help(program_name):
    """
    Print a custom help message and exit.

    Arguments: 
        program_name (str): name of the current program to use.
    """
    help_message = f"""
 ____      __     __              
|  _ \\ _   \\ \\   / /__ _ ____   __
| |_) | | | \\ \\ / / _ \\ '_ \\ \\ / /
|  __/| |_| |\\ V /  __/ | | \\ V / 
|_|    \\__, | \\_/ \\___|_| |_|\\_/  
       |___/                      

help: {program_name} <command> [arguments]

Global Options:
    -h, --help               Show this help message and exit.
    
Commands:
    
    create                   Create a new environment.
        Options: {program_name} create <environment name>

    remove                   Delete an environment.
        Options: {program_name} remove <environment name>

    shell                    Activate an environment.
        Options: {program_name} activate <environment name>

    """
    print(help_message)
    exit(1)

def parse_args():
    """
    Custom parser to check if arguments match the requirements.
    """
    program_name, args = 'pyvenv', sys.argv[1:]
    exit = False

    if "-h" in args or "--help" in args:
        exit = True
    elif args[0] != "create" and args[0] != "remove" and args[0] != "shell":
        exit = True
    elif len(args) != 2:
        exit = True

    if exit:
        print_help(program_name)
    
    return args