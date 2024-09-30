# _tests_/test_calculadora.py

import pytest
from calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(1, 2) == 3

def test_subtracao():
    assert subtracao(4, 2) == 2

def test_multiplicacao():
    assert multiplicacao(3, 3) == 9

def test_divisao():
    assert divisao(10, 2) == 5

def test_zero_division():
    with pytest.raises(ValueError):
        divisao(1, 0)
