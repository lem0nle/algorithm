class _Node:
    def __init__(self, obj, n):
        self.obj, self.n = obj, n


class _BiNode:
    def __init__(self, obj, p, n):
        self.obj, self.p, self.n = obj, p, n


class _NodeIter:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        if self.node is None:
            raise StopIteration()
        obj = self.node.obj
        self.node = self.node.n
        return obj


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return _NodeIter(self.head)

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
        p = self.head.n
        self.head.n = None
        while p is not None:
            temp = p.n
            p.n = self.head
            self.head = p
            p = temp


class LinkedListFakeNode(LinkedList):
    def __init__(self):
        super().__init__()
        self._head = _Node(None, None)

    def insert(self, obj, index=0):
        node = self._head
        for _ in range(index):
            node = node.n
        node.n = _Node(obj, node.n)

    def remove(self, index):
        node = self._head
        for _ in range(index):
            node = node.n
        node.n = node.n.n

    @property
    def head(self):
        return self._head.n

    @head.setter
    def head(self, v):
        pass

    def reverse(self):
        pnode = None
        node = self.head
        while node is not None:
            temp = node.n
            node.n = pnode
            pnode = node
            node = temp
        self._head.n = pnode


if __name__ == '__main__':
    ll = LinkedListFakeNode()
    ll.insert('once')
    ll.insert('upon')
    ll.insert('a')
    ll.insert('time')
    ll.reverse()
    print(ll)
    ll.remove(2)
    ll.insert('b', 2)
    for item in ll:
        print(item)
