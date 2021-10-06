# Nose

import E4

def test_add():
    assert E4.add(2, 5) == 7
    assert E4.add(-9, 5) == -4

def test_substract():
    assert E4.substract(-10, 5) == -15
    assert E4.substract(9, 1) == 8

def test_multiplay():
    assert E4.multiplay(3, 5) != 33 
    assert E4.multiplay(3, -9) == -27

def test_division():
    assert E4.division(10, 2) == 5
    assert E4.division(9, 3) == 3


