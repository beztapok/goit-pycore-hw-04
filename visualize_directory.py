import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізуємо colorama для коректної роботи на Windows
init(autoreset=True)

def visualize_directory(path, indent_level=0):
    try:
        path_obj = Path(path)
        if not path_obj.exists():
            print(Fore.RED + "Шлях не існує.")
            return
        if not path_obj.is_dir():
            print(Fore.RED + "Це не директорія.")
            return

        for item in path_obj.iterdir():
            if item.is_dir():
                print(" " * indent_level + Fore.BLUE + item.name + "/")
                visualize_directory(item, indent_level + 4)
            else:
                print(" " * indent_level + Fore.GREEN + item.name)

    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python visualize_directory.py ./goit-pycore-hw-04")
        return

    directory_path = sys.argv[1]
    visualize_directory(directory_path)

if __name__ == "__main__":
    main()
