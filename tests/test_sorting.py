import pytest
from algo.sorting import heapSort


def test_heap_sorting():
    array = [2, 0, 1, 8, 0, 5, 2, 3]
    heapSort(array)
    assert array == sorted(array)

    heapSort(array, reverse=True)
    assert array == sorted(array, reverse=True)
