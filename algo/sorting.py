from .heap import Heap


def heapSort(array, reverse=False):
    if reverse:
        heap = Heap(array)
    else:
        heap = Heap(array, lambda a, b: a > b)
    for _ in range(len(array)):
        heap.pop()
