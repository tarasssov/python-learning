# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def opros(name, age, city):
    text = name + ', ' + age + ' год(а), проживает в городе ' + city
    return text

name = input('Как зовут Человека?')
age = input('Сколько лет?')
city = input('В каком городе проживает?')

print(opros(name, age, city))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def maxim(q, w, e):
    max = q
    if max < w:
        max = w
    if max < e:
        max = e
    return max
a = input ('a:')
b = input('b:')
c = input('c:')
print('ваши числа', a, b, c)
print('Наибольшее - ', maxim(a,b,c))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

k= []

def maxim(*args):
    maxus = max(*args)
    return maxus

k.append(input ('a:'))
k.append(input ('b:'))
k.append(input ('c:'))
print('ваши числа', k)
print('Наибольшее - ', maxim(k))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def maxlint(*args):
    longstr = max(args,key = len)
    return longstr