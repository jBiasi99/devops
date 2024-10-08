# _tests_/test_calculadora.py

import pytest  # Adicione esta linha
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
