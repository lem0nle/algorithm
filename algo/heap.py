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

    def _swim(self, k):
        heap = self.heap
        cmp = self.cmp
        while k != 0 and cmp(heap[k], heap[(k - 1) // 2]):
            temp = heap[k]
            heap[k] = heap[(k - 1) // 2]
            heap[(k - 1) // 2] = temp
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
            temp = heap[k]
            heap[k] = heap[j]
            heap[j] = temp
            k = j

    def top(self):
        return self.heap[0]

    def pop(self):
        self.size -= 1
        heap = self.heap
        top = heap[0]
        heap[0] = heap[self.size]
        heap[self.size] = top
        self._sink(0)
        return top
