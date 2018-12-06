from .stack import Stack


def checkBrackets(s):
    """Check if the brackets in a string are matching."""
    stack = Stack()
    d = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in set(')]}'):
            if not len(stack) or stack.top() != d[c]:
                return False
            stack.pop()
        elif c in set('([{'):
            stack.push(c)
    return len(stack) == 0
