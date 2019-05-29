import pytest

from solution import solution

def test_None():
    with pytest.raises(ValueError, match="N is None"):
        solution(None)

def test_None():
    with pytest.raises(TypeError, match="N must to be int, not a float"):
        solution(4.2)

def test_None():
    with pytest.raises(ValueError, match="N value must to be greater tham 0"):
        solution(-1)

def test_None():
    assert solution(3) == 6