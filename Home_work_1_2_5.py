# Реализуйте алгоритм перемешивания списка.
import random
List1 = [1, 2, 3, 4, 5]
print('Изначальный список', List1)
for i in range(len(List1)-1, 0, -1):
    j = random.randint(0, i + 1)
    List1[i], List1[j] = List1[j], List1[i]
print('Случайно перемешанный список', List1)
