# 1) Иван Васильевич = арбуз = для себя и для тещи. Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса арбуза 
# 2) Пользователь вводит одно число N.  Далее идут N чисел, записанных на новой строчке каждое. 
# Вывести максимальное и минимальное (циклы) Input:	5 -> 5 1 6 5 9   Output:	1 9

# weight - вес; watermelon - арбуз;

from random import randint

watermelon = int(input('Введите колличество арбузов: '))
weight = randint(1, 22)
print(weight, end = ' ')

max_weight = weight
min_weight = weight
for _ in range(watermelon -1):
    weight = randint(1, 22)
    print(weight, end = ' ')
    max_weight = max(weight, max_weight)
    min_weight = min(weight, min_weight)
print()
print()
print(min_weight, max_weight)
print()

    
 
    
