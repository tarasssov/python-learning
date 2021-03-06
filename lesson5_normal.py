# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import lesson5_easy
import sys
import os


try:
    if sys.argv[1] == 'help':
        print(''' 
        1. Перейти в папку
        2. Просмотреть содержимое текущей папки
        3. Удалить папки dir_1 - dir_9
        4. Создать папку''')


    if sys.argv[1] == '1':
        lesson5_easy.perehod()
        print('Успешно перешли : ' , os.getcwd())



    elif sys.argv[1] == '2':
        lesson5_easy.show_dir()

    elif sys.argv[1] == '3':
        print ('Удаляем папку из текущей директории.')
        fold = input('Введи название папки - ')
        lesson5_easy.deldir(fold)
        print('Успешно удалено')

    elif sys.argv[1] == '4':
        print('Создаем папку в текущей директории.')
        fold = input('Введи название папки - ')
        lesson5_easy.makedir(fold)
        print('Успешно создано')
    else:
        print('Вводи правильный индекс')

except IndexError:
    print('Должен быть хоть один индекс')

except FileNotFoundError:
    print('Невозможно перейти. Нет такой папки.')
except:
    print('Невозможно создать/удалить/перейти')


