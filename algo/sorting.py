from .heap import Heap


def heapSort(array, reverse=False):
    if reverse:
        heap = Heap(array)
    else:
        heap = Heap(array, lambda a, b: a > b)
    for _ in range(len(array)):
        heap.pop()


def quickSort(array, low=0, high=None):
    """O(n*log n)"""
    if high is None:
        high = len(array)
    if high - low <= 1:
        return
    p = low
    for i in range(low, high - 1):
        if array[i] < array[high - 1]:
            temp = array[p]
            array[p] = array[i]
            array[i] = temp
            p += 1
    temp = array[p]
    array[p] = array[high - 1]
    array[high - 1] = temp
    quickSort(array, low, p)
    quickSort(array, p + 1, high)
