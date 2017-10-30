# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

#print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - копирует файл')
    print('rm <file_name> - удаляет файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not file_name_to_copy:
        print('Укажите имя файла для копирования вторым параметром')
        return
    try:
        shutil.copy(file_name_to_copy,file_name_to_copy + '_copy')
        print('Файл {} удачно скопирован'.format(file_name_to_copy))
    except IOError:
        print('Упс. Что-то с копированием файла {} пошло не так.'.format(file_name_to_copy))

def del_file():
    if not file_name_to_delete:
        print('Укажите имя файла для удаления вторым параметром')
        return
    try:
        if input('Уверены что хотите удалить файл? - {} Y/N'.format(file_name_to_delete)) == "Y":
            os.remove(file_name_to_delete)
        else:
            pass
    except:
        print('Упс. Что-то с удалением файла {} пошло не так.'.format(file_name_to_delete))

def change_dir():
    if not chdir_path:
        print('Укажите имя папки или полный путь для перемещения вторым параметром')
        return
    try:
        print('Ваша текущая категория', os.path.abspath(chdir_path))
        os.chdir(os.path.abspath(chdir_path))
    except:
        print('Упс. Что-то с переходом в категорию {} пошло не так.'.format(chdir_path))
def current_path():
    print('Полный путь до категории где вы находитесь - ', os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp":copy_file,
    "rm":del_file,
    "cd":change_dir,
    "ls":current_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    file_name_to_copy = sys.argv[2]
except IndexError:
    file_name_to_copy = None

try:
    file_name_to_delete = sys.argv[2]
except IndexError:
    file_name_to_delete = None

try:
    chdir_path = sys.argv[2]
except IndexError:
    chdir_path = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")