# import pytest 

def test_calc_addition():
    # Fonction de test du résultat de 2 + 4
    output = 2 + 4
    assert output == 6


def test_calc_subtraction():
    # Fonction de test du résultat de 2 - 4
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    # Fonction de test du résultat de 2 * 4
    output = 2 * 4
    assert output == 8


def test_coucou():
    # Fonction de test si le résultat renvoie 'hello'
    output = "hello"
    assert output == "hello"
