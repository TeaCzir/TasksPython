# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны 
# нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону 
# едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и 
# обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это 
# сделать невозможно. Input: 3 4(ввод на разных строках) Output: 6

i = int(input('Введите № вагона по счету с головы: '))
j = int(input('Введите действительный № вагона: '))

if (i == j):
    print('Недостаточно информации.')
else:
    c = i + j - 1
    print('Колличество вагонов:', c)
    



