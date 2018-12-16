class _Node:
    def __init__(self, obj, n):
        self.obj, self.n = obj, n


class _BiNode:
    def __init__(self, obj, p, n):
        self.obj, self.p, self.n = obj, p, n


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        pass

    def insert(self, obj, index=0):
        if index < 0:
            index = self.length + index
        index = max(index, 0)
        index = min(index, self.length)
        self.length += 1

        if index == 0:
            self.head = _Node(obj, self.head)
            return

        p = self.head
        for _ in range(index - 1):
            p = p.n
        p.n = _Node(obj, p.n)

    def remove(self, index):
        if index < 0:
            index = self.length + index
        index = max(index, 0)
        index = min(index, self.length - 1)
        self.length -= 1

        if index == 0:
            self.head = self.head.n
            return

        p = self.head
        for _ in range(index - 1):
            p = p.n
        p.n = p.n.n

    def find(self, obj):
        p = self.head
        for i in range(self.length):
            if p.obj == obj:
                return i
            p = p.n
        return -1

    def reverse(self):
        pass


class LinkedListFakeNode:
    def __init__(self):
        self.head = _Node(None, None)

    def insert(self, obj, index=0):
        node = self.head
        for _ in range(index):
            node = node.n
        node.n = _Node(obj, node.n)

    def remove(self, index):
        node = self.head
        for _ in range(index):
            node = node.n
        node.n = node.n.n
