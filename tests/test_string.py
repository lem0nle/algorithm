import pytest
from algo.string import checkBrackets, evaluate


def test_check_brackets():
    assert checkBrackets('s(t{r}i[]ng)')

    assert not checkBrackets('st(r[[i]n)g}')

    assert not checkBrackets(']string')

    assert not checkBrackets('s(t[r{)}i]ng')


def test_evaluate():
    expr = '(1-(2+3)*4)/5'
    assert evaluate(expr) == -3.8

    expr = '1 - 2 + 3'
    assert evaluate(expr) == 2

    with pytest.raises(AssertionError) as e:
        evaluate('((1+2)/3')
        assert e.message == 'operators not empty'

    with pytest.raises(AssertionError) as e:
        evaluate('1+2*(')
        assert e.message == 'more than one values left'

    with pytest.raises(AssertionError) as e:
        evaluate(')')
        assert e.message == 'more ")" than "("'
