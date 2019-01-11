from ..recursion import hanoi


def test_hanoi():
    assert len(hanoi(1, 2, 3, 3)) == 7
    assert len(hanoi(1, 2, 3, 5)) == 31
