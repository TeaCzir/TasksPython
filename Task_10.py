'''Задача 10 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
Пример: 5 -> 1 0 1 1 0    2 '''

from random import randint

n = int(input('Введите общее колличество монет: '))

list_coins = []
for i in range(n):
    list_coins.append(randint(0, 1))
print(list_coins)
zero = list_coins.count(0)
if len(list_coins) - zero < zero:
    print(f'Нужно повернуть {len(list_coins) - zero} монет. Со значением: 1')
else:
    print(f'Нужно повернуть {zero} монет. Со значением: 0')



