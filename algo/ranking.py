from random import randint


def topk(array, k, largest=True, low=0, high=None):
    if high is None:
        high = len(array)
    if high - low <= 1:
        return array[low:high]

    if largest:
        def cmp(a, b):
            return a > b
    else:
        def cmp(a, b):
            return a < b

    p = low
    ind = randint(low, high - 1)
    array[ind], array[high - 1] = array[high - 1], array[ind]

    for i in range(low, high - 1):
        if cmp(array[i], array[high - 1]):
            array[i], array[p] = array[p], array[i]
            p += 1
    array[p], array[high - 1] = array[high - 1], array[p]

    n = p - low + 1
    if n == k:
        return array[low:p + 1]
    if n > k:
        return topk(array, k, largest, low, p)
    else:
        return array[low:p + 1] + topk(array, k - n, largest, p + 1, high)


if __name__ == '__main__':
    a = [1, 2, 5, 2, 1, 7, 8, 3, 9]
    print(topk(a, 6, False))
