from .linked import LinkedList


def binarySearch(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == item:
            return mid
        if array[mid] > item:
            high = mid - 1
        elif array[mid] < item:
            low = mid + 1
    return -1


class Set:
    def __init__(self, it):
        self.Q = 997
        self.hash_table = [LinkedList() for _ in range(self.Q)]
        self.length = 0
        for obj in it:
            self.add(obj)

    def __len__(self):
        return self.length

    def __contains__(self, obj):
        ind = hash(obj) % self.Q
        return obj in self.hash_table[ind]

    def add(self, obj):
        ind = hash(obj) % self.Q
        if obj not in self.hash_table[ind]:
            self.hash_table[ind].insert(obj)
            self.length += 1
