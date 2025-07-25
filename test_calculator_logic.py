import calculator_logic as c
import pytest


#Первая функция для тестировани сложения
def test_add():
    assert c.add(10, 5) == 15#просим протестировать значения
    assert c.add(-1, 1) == 0
    assert c.add(-1, -1) == -2

    with pytest.raises(TypeError): #обработка исключений
        c.add('text', 5) #проверка этой ошибки

    with pytest.raises(TypeError): #обработка исключений
        c.add(5, 'txt')

def test_subtract():
    assert c.subtract(10, 5) == 5#просим протестировать значения
    assert c.subtract(-1, 1) == -2
    assert c.subtract(-10, -10) == 0

    with pytest.raises(TypeError): #обработка исключений
        c.subtract('text', 5) #проверка этой ошибки

    with pytest.raises(TypeError): #обработка исключений, что текст на чисо нельзя
        c.subtract(5, 'text')


def test_multiply():
    assert c.multiply(10, 5) == 50#просим протестировать значения
    assert c.multiply(-1, 1) == -1
    assert c.multiply(-10, -10) == 100



def test_divide():
    assert c.divide (10, 5) == 2 #просим протестировать значения
    assert c.divide (-10, 2) == -5
    assert c.divide (-10, -2) == 5

    with pytest.raises(TypeError): #обработка исключений
        c.divide('text', 5) #проверка этой ошибки

    with pytest.raises(TypeError): #обработка исключений
        c.divide(5, 'text')

    with pytest.raises(ZeroDivisionError): #нельзя делить на ноль
        c.divide(10, 0)


def test_square():
    assert c.square(10) == 100
    assert c.square(0) == 0
    assert c.square(-10) == 100


test_add()#вызываем функцию
test_subtract()
test_multiply()
test_divide()
test_square()
print("Тесты пройдены успешно")