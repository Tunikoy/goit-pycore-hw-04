# directory_structure.py

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)

def display_directory_structure(directory_path):
    try:
        path = Path(directory_path)
        if not path.is_dir():
            print(f"{Fore.RED}Помилка: {directory_path} не є директорією.")
            return

        print(f"{Fore.GREEN}Структура директорії {path.resolve()}:\n")

        # Обхід директорій і файлів
        for item in path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"Директорія: {item.name}")
            elif item.is_file():
                print(Fore.YELLOW + f"Файл: {item.name}")
            else:
                print(f"Інший об'єкт: {item.name}")

    except FileNotFoundError:
        print(f"{Fore.RED}Помилка: Директорію {directory_path} не знайдено.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED} шлях до директорії.")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)
    
# python exercise_3.py /Users/a1234/Projects/my_directory