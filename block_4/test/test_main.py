import pytest
from block_4.src.main import *


@pytest.mark.parametrize(
    ["s1", "s2", "res"],
    [
        ("Хочу на", "шину", "Хочу на шину"),
        ("Когда можно", "просить повышение?", "Когда можно просить повышение?"),
        ("Когда можно", "стать начальником Умалата?", "Когда можно стать начальником Умалата?"),
    ]
)
def test_concatenation(s1, s2, res):
    result = concatenation(s1, s2)
    print("\n" + result)
    assert result == res