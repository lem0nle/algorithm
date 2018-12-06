class Stack:
    """Implement push and pop operations for stack."""

    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
