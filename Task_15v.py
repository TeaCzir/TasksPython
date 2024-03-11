
from random import randint

watermelon = int(input('Введите колличество арбузов: '))
weight = randint(1, 17)
print(weight, end = ' ')
# max_weight = float("inf") # бесконечность. ВЫВОДИТ: inf
# min_weight = -float("inf") # бесконечность. ВЫВОДИТ: -inf
# max_weight = float(1, 17) # бесконечность. ВЫВОДИТ: TypeError: float expected at most 1 argument, got 2
# min_weight = -float(1, 17) # бесконечность. ВЫВОДИТ: TypeError: float expected at most 1 argument, got 2
max_weight = weight
min_weight = weight

for _ in range(watermelon):
    weight = randint(1, 17)
    print(weight, end = ' ')
    #if max_weight < weight: БЕЗ РАЗНИЦЫ.
    if weight > max_weight:
        max_weight = weight
    #if min_weight > weight: БЕЗ РАЗНИЦЫ.
    if weight < min_weight:
        min_weight = weight

print()
print()
print(min_weight, max_weight)
print()

