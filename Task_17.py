# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]     Output: 6

from random import randint

size = int(input('Введите количество элементов в списке: '))

# list_1 = []

# for _ in range(size):
#     num = randint(-10, 10)
#     list_1.append(num)
# print(*list_1)

list_1 = [randint(-10, 10) for _ in range(size)]

print(list_1)
print(set(list_1))
print(len(set(list_1)))

# 2
list2 = []

for num in list_1:
    if num not in list2:
        list2.append(num)
print(list2)
print(len(list2))


