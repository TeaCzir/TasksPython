# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

size = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число "х": '))

cot = 0

for _ in range(size):
    list_1 = [randint(1, 7)]
    print(*list_1, end = ' ')
    for i in range(len(list_1)):
        if list_1[i] == x:
            cot += 1

print()
print(f'Вы ввели значение: {x}')
print(f'Элементов со значением {x} встречается в массиве {cot} раз.')
     


