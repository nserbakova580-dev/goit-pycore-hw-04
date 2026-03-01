#Треба: розробити скрипт: приймає шлях до директорії
#в якості аргументу командного рядка і 
#візуалізує структуру цієї директорії, 
#виводячи імена всіх піддиректорій та файлів. 
#Для кращого візуального сприйняття: 
#імена директорій та файлів відрізняються за кольором

import sys #шлях до директорії як аргумент командного рядка
from pathlib import Path #робота з файловою системою
import colorama as clr #кольорове форматування виводу

def print_tree(directory: Path, indent: str ="") -> None:

    try:
        entries = sorted(directory.iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
    except PermissionError:
        print(indent + clr.Fore.RED + "Permission denied" + clr.Style.RESET_ALL)
        return

    for entry in entries:
        if entry.is_dir():
            print(indent + clr.Fore.BLUE + entry.name + clr.Style.RESET_ALL) 
            print_tree(entry, indent + "    ")
        else:
            print(indent + clr.Fore.GREEN + entry.name + clr.Style.RESET_ALL)

def main():
    clr.init(autoreset=True)

    if len(sys.argv) != 2: #перевірка наявності 2-го аргумента
        print("Usage: python dir_tree.py <directory_path>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists(): #перевірка наявності шляху 
        print(clr.Fore.RED + "Error: Path doesn't exist")
        sys.exit(1)

    if not path.is_dir(): 
        print(clr.Fore.RED + "Error: Path isn't a directory")
        sys.exit(1)

    print(clr.Fore.CYAN + f"\nDirectory structure of {path}\n")
    print_tree(path)

if __name__ == "__main__":
    main()
     


