class Heap:
    """Heap."""

    def __init__(self):
        self.heap = []

    def _swim(self, k):
        heap = self.heap
        while k != 0 and heap[(k - 1) // 2] > heap[k]:
            temp = heap[k]
            heap[k] = heap[(k - 1) // 2]
            heap[(k - 1) // 2] = temp
            k = (k - 1) // 2

    def _sink(self, k):
        heap = self.heap
        while 2 * k + 1 < len(heap):
            j = 2 * k + 1
            if j + 1 < len(heap) and heap[j + 1] < heap[j]:
                j += 1
            if heap[k] <= heap[j]:
                break
            temp = heap[k]
            heap[k] = heap[j]
            heap[j] = temp
            k = j
