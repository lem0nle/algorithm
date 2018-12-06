from algo.string import checkBrackets


def test_check_brackets():
    assert checkBrackets('s(t{r}i[]ng)')

    assert not checkBrackets('st(r[[i]n)g}')

    assert not checkBrackets(']string')

    assert not checkBrackets('s(t[r{)}i]ng')
