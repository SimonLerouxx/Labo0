"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from src.calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    my_calculator = Calculator()

    result = my_calculator.addition(5, 3)

    assert result == 8
    assert my_calculator.last_result == 8


def test_subtraction():
    my_calculator = Calculator()

    result = my_calculator.subtraction(10, 4)

    assert result == 6
    assert my_calculator.last_result == 6


def test_multiplication():
    my_calculator = Calculator()

    result = my_calculator.multiplication(6, 7)

    assert result == 42
    assert my_calculator.last_result == 42


def test_division():
    my_calculator = Calculator()

    result = my_calculator.division(20, 5)

    assert result == 4
    assert my_calculator.last_result == 4