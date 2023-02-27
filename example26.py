"""
Напишите программу, которая на вход принимает два числа a и b
и возводит число a в целую степень b с помощью рекурсии.
"""


def exponentiation(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * exponentiation(a, b - 1)


a = int(input("Введите число: "))
b = int(input("Введите значение степени: "))
print(f"Результат возведения числа в степень равен: {exponentiation(a, b)}")
