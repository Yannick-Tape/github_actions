import math
import random
import numpy as np


def test_calc_addition():
    # Fonction de test du résultat de 2 + 4
    output = 2 + 4
    assert output == 6


def test_numpy():
    a = np.array([1, 2, 3, 4, 5])
    output = np.sum(a)
    assert output == 15


def test_square():
    output = math.log(1)
    assert output == 0
    

def test_randint():
    output = random.randint(1, 1)
    assert output == 1
    

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
