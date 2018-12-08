"""String algorithms."""
from .stack import Stack


def checkBrackets(s):
    """Check if the brackets in a string are matching."""
    stack = Stack()
    d = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in ')]}':
            if not len(stack) or stack.top() != d[c]:
                return False
            stack.pop()
        elif c in '([{':
            stack.push(c)
    return len(stack) == 0


def _calc(op, a, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b


def evaluate(expr):
    """Evaluate arithmetic expressions."""
    expr = '(' + expr + ')'
    vals = Stack()
    ops = Stack()
    d = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': -1}
    for c in expr:
        if c.isspace():
            continue
        if c in d.keys():
            while len(ops) and d[ops.top()] >= d[c] and ops.top() != '(':
                assert len(vals) >= 2, 'lacking oprands'
                op = ops.pop()
                b = vals.pop()
                a = vals.pop()
                vals.push(_calc(op, a, b))
            if c == ')':
                assert len(ops), 'more ")" than "("'
                ops.pop()
            else:
                ops.push(c)
        else:
            vals.push(int(c))
    assert len(vals) == 1, 'more than one values left'
    assert len(ops) == 0, 'operators not empty'
    return vals.top()


if __name__ == '__main__':
    print(evaluate('3(1+3)'))
