from calculator import add, sub, mul, div
import pytest

def test_ops():
    assert add(4, 2) == 6
    assert sub(6, 4) == 2
    assert mul(7, 9) == 63
    assert div(4, 2) == 2

def test_div_zero():
    with pytest.raises(ValueError):
        div(1, 0)