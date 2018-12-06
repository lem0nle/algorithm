import pytest
from algo.stack import Stack


def test_stack():
    s = Stack()
    assert len(s) == 0

    s.push(0)
    s.push(1)
    assert s.top() == 1
    assert str(s) == '[0, 1]'
    assert s.pop() == 1
    assert len(s) == 1

    s.pop()

    with pytest.raises(IndexError):
        s.top()

    with pytest.raises(IndexError):
        s.pop()
