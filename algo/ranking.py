from random import randint
from .heap import Heap


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


class RankingList:
    def __init__(self, k):
        self.k = k
        self.array = []
        self.topk = None

    def append(self, item):
        if self.array is not None:
            if len(self.array) < self.k:
                self.array.append(item)
            if len(self.array) == self.k:
                self.topk = Heap(self.array)
                self.array = None
        else:
            if self.topk.top() < item:
                self.topk.editroot(item)

    def ranking(self):
        if self.array is None:
            return list(sorted(self.topk.heap, reverse=True))
        else:
            return list(sorted(self.array, reverse=True))


if __name__ == '__main__':
    a = [1, 2, 5, 2, 1, 7, 8, 3, 9]
    rl = RankingList(5)
    for i in a:
        rl.append(i)
    print(rl.ranking())
