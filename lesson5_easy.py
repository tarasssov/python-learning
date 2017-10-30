# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

def makedir(fold):
    os.mkdir(fold)

def make9dir():
    for x in range(9):
        os.mkdir('dir_{}'.format(x+1))

if __name__ == '__main__':
    make9dir()
    input()

def deldir(fold):
    os.rmdir(fold)

def del9dir():
    for x in range(9):
        os.rmdir('dir_{}'.format(x+1))

if __name__ == '__main__':
    del9dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dir():
    print(os.listdir())

if __name__ == '__main__':
    show_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    shutil.copy('lesson5_easy.py', 'lesson5_easy_copy.py')

if __name__ == '__main__':
    copy_file()

def perehod():
    d = os.getcwd()
    print('Сейчас вы тут - ', d)
    d = input('Куда хотите перейти? : ')
    os.chdir(os.path.join(os.getcwd(),d))