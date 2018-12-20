import pytest
from algo.sorting import heapSort, quickSort


def test_heap_sorting():
    array = [2, 0, 1, 8, 0, 5, 2, 3]
    heapSort(array)
    assert array == sorted(array)

    heapSort(array, reverse=True)
    assert array == sorted(array, reverse=True)


def test_quick_sorting():
    array = [2, 0, 1, 8, 0, 5, 2, 3]
    quickSort(array)
    assert array == sorted(array)
