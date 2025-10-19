import sys
from pathlib import Path
from colorama import Fore

def iterate_folder(path, tree = ""):
    lists = list(path.iterdir())
    for el in lists:
        if el.is_dir():
            print(Fore.BLUE + f"{tree + el.name + "/"}")
            indent = "    "
            iterate_folder(el, indent + tree)
        else:
            print(Fore.GREEN + f"{tree + el.name}")

try:
    # python ./task_3/main.py ./task_3 - ось так потрібно запускати
    p = Path(sys.argv[1])
    iterate_folder(p)
except Exception as err:
    print(err)