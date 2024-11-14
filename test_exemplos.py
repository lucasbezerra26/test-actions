
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0



















def multiplica(a, b):
    return a * b

import pytest

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (1, 0, 0),
    (-1, 5, -5),
    (10, 10, 100)
])
def test_multiplica(a, b, resultado):
    assert multiplica(a, b) == resultado



# Código para testar
def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="Divisão por zero!"):
        divide(10, 0)






def subtrai(a, b):
    return a - b

import pytest

@pytest.fixture
def valores():
    return (10, 3)

def test_subtrai(valores):
    a, b = valores
    assert subtrai(a, b) == 7