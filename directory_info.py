import os
import logging
import argparse
from collections import namedtuple

# Определение namedtuple для хранения информации о файлах и директориях
FileInfo = namedtuple('FileInfo', 'name extension is_dir parent_dir')

# Настройка логирования
logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(message)s')


def collect_directory_info(directory_path):
    directory_contents = []

    for root, dirs, files in os.walk(directory_path):
        parent_dir = os.path.basename(root)

        # Обработка директорий
        for dir_name in dirs:
            directory_contents.append(FileInfo(name=dir_name, extension='', is_dir=True, parent_dir=parent_dir))

        # Обработка файлов
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            extension = extension.lstrip('.')  # Убираем точку перед расширением
            directory_contents.append(FileInfo(name=name, extension=extension, is_dir=False, parent_dir=parent_dir))

    return directory_contents


def log_directory_info(directory_contents):
    for item in directory_contents:
        logging.info(
            f"Name: {item.name}, Extension: {item.extension}, Is Directory: {item.is_dir}, Parent Directory: {item.parent_dir}")


def main():
    parser = argparse.ArgumentParser(description='Collect directory contents information.')
    parser.add_argument('directory_path', type=str, help='Path to the directory')
    args = parser.parse_args()

    directory_path = args.directory_path
    if not os.path.isdir(directory_path):
        print(f"The provided path '{directory_path}' is not a valid directory.")
        return

    directory_contents = collect_directory_info(directory_path)
    log_directory_info(directory_contents)
    print(f"Directory contents have been logged to 'directory_contents.log'.")


if __name__ == '__main__':
    main()