# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

size = int(input('Введите количество элементов массива: '))
x = int(input('Введите заданное число: '))

list1 = [randint(1, 10) for _ in range(size)]
print(list1)
y = abs(x - list1[0]) # модуль числа - дает всегда положительный результат.
clous = list1[0]
for i in range(1, len(list1)):    
    if y > abs(x - list1[i]):
        y = abs(x - list1[i])
        clous = list1[i]
print(clous)
    


