def add(a, b): #сложение
    return a + b


def subtract(a, b): #вычитание
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError ('Деление на ноль!')#исключения
    return a / b


def square(x):
    return x ** 2

