class Heap:
    """Heap."""

    def __init__(self, array=None, cmp=None):
        if cmp is None:
            def cmp(a, b):
                return a < b
        self.cmp = cmp
        if array is None:
            array = []
        self.size = len(array)
        self.heap = array
        for i in range(self.size):
            self._sink(self.size - i - 1)

    def __len__(self):
        return self.size

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def _swim(self, k):
        # k is the index in heap.
        heap = self.heap
        cmp = self.cmp
        while k != 0 and cmp(heap[k], heap[(k - 1) // 2]):
            self._swap(k, (k - 1) // 2)
            k = (k - 1) // 2

    def _sink(self, k):
        heap = self.heap
        cmp = self.cmp
        while 2 * k + 1 < self.size:
            j = 2 * k + 1
            if j + 1 < self.size and cmp(heap[j + 1], heap[j]):
                j += 1
            if not cmp(heap[j], heap[k]):
                break
            self._swap(k, j)
            k = j

    def top(self):
        return self.heap[0]

    def pop(self):
        self.size -= 1
        self._swap(0, self.size)
        self._sink(0)
        return self.heap[self.size]

    def editroot(self, e):
        self.heap[0] = e
        self._sink(0)


class PQ(Heap):
    def __init__(self, cmp=None):
        def new_cmp(a, b):
            return a[1] < b[1] if cmp is None else cmp(a[1], b[1])
        super().__init__([], new_cmp)
        self.ind = []

    def __contains__(self, ind):
        # customize 'in'
        return len(self.ind) > ind and self.ind[ind] is not None

    def _swap(self, i, j):
        super()._swap(i, j)
        temp = self.ind[self.heap[i][0]]
        self.ind[self.heap[i][0]] = self.ind[self.heap[j][0]]
        self.ind[self.heap[j][0]] = temp

    def insert(self, ind, item):
        self.heap.append([ind, item])

        if ind >= len(self.ind):
            t = ind - len(self.ind)
            self.ind.extend([None] * t)
            self.ind.append(self.size)
        else:
            self.ind[ind] = self.size

        self._swim(self.size)
        self.size += 1

    def edit(self, ind, item):
        self.heap[self.ind[ind]][1] = item
        self._swim(self.ind[ind])
        self._sink(self.ind[ind])

    def pop(self):
        super().pop()
        ind, item = self.heap.pop()
        self.ind[ind] = None
        return ind, item
