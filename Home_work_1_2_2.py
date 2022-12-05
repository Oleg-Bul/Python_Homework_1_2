import math

# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число '))
factorialList = []
factorial = 1
for i in range(1, n+1):
    factorial *= i
    factorialList.append(factorial)
print(factorialList)

# Решение от преподователя


def mult(n: int) -> str:
    """ Возвращает строку произведений """
    str_mult = '1'
    for i in range(2, n+1):
        if i == n:
            str_mult += f'*{i}'
        else:
            str_mult += f'*{i}'
    return str_mult


n = int(input('Num: '))
multiplications = [math.factorial(i) for i in range(1, n+1)]
multiplications_string = [mult(i) for i in range(1, n+1)]
print(f"List of multiplication: {multiplications}")
print(f"List: {multiplications_string}")
