# Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите вещественное число ').replace(".", "")
list1 = [int(i) for i in n]
sum = 0
for j in range(len(list1)):
    sum = list1[j]+sum
print('Сумма цифр в числе равна: ', sum)


# Решение от преподователя

# number = input('Num:')
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print(f'Sum of nums: {sum}')
