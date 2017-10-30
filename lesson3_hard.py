# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

'''player = {'name':'', 'health' :100,'damage' :50}
enemy = {'name':'', 'health' :100,'damage' :50}

player ['name'] = input('Введи имя игрока - ')
enemy ['name'] = input('Введи имя врага - ')

def attack (player,enemy):
    enemy ['health'] = enemy ['health'] - player['damage']
    return player , enemy'''

#attack(player,enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player = {'name':'', 'health' :100,'damage' :50, 'armor':1.2}
enemy = {'name':'', 'health' :100,'damage' :50, 'armor':1.2}

player ['name'] = input('Введи имя игрока - ')
enemy ['name'] = input('Введи имя врага - ')
p_damage = player['damage']
e_armor = enemy ['armor']

def damage_vs_armor (p_damage, e_armor):
    p_damage = p_damage / e_armor
    return (p_damage)

def attack (player,enemy):
    enemy ['health'] = enemy ['health'] - damage_vs_armor(p_damage, e_armor)
    return player , enemy

file_player = player['name'] + ', .py.txt'
with open(file_player, 'w',encoding='utf-8') as f_p:
    f_p.write(str(player))


#print (attack(player , enemy))

