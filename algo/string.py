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


def shash(s, R=10, Q=997):
    h = 0
    for c in s:
        h = (R * h + ord(c)) % Q
    return h


def find(s, sub):
    M = len(sub)
    if M > len(s):
        return -1

    R, Q = 10, 997
    delta = 1
    for i in range(M - 1):
        delta = delta * R % Q

    h_sub = shash(sub, R, Q)
    h_s = shash(s[:M], R, Q)

    if h_s == h_sub and s[:M] == sub:
        return 0

    for i in range(1, len(s) - M + 1):
        h_s = ((h_s - ord(s[i - 1]) * delta) * R + ord(s[i + M - 1])) % Q
        if h_s == h_sub and s[i:i + M] == sub:
            return i

    return -1


if __name__ == '__main__':
    print(find('adedczsf', 'dc'))
