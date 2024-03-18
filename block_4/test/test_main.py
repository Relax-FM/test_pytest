import pytest
from block_4.src.main import *
from contextlib import nullcontext as ex_not_raise
import pytest


@pytest.mark.parametrize(
    ["s1", "s2", "res", "ex"],
    [
        ("Hello", "World", "HelloWorld", ex_not_raise()),
        ("te", "st", "test", ex_not_raise()),
        ("", "", "", ex_not_raise()),
        ("string1", "string2", "string1string2", ex_not_raise()),
        (1555, "string2", "", pytest.raises(TypeError)),
        ("string1", 1234, "", pytest.raises(TypeError)),
        (4321, 1234, "", pytest.raises(TypeError)),
    ]
)
def test_concatenation(s1, s2, res, ex):
    with ex:
        assert concatenation(s1, s2) == res