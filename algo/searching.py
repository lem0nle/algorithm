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

    def __str__(self):
        return '{' + ', '.join(repr(c) for c in self) + '}'

        """another way to implement __str__()"""
        # from io import StringIO
        # buff = StringIO()
        # buff.write('{')
        # for li in self.hash_table:
        #     for i in li:
        #         buff.write(repr(i))
        #         buff.write(', ')
        # buff.seek(buff.tell() - 2)
        # buff.write('}')
        # return buff.getvalue()[:-1]

    def __iter__(self):
        for li in self.hash_table:
            for i in li:
                yield i

    def add(self, obj):
        ind = hash(obj) % self.Q
        if obj not in self.hash_table[ind]:
            self.hash_table[ind].insert(obj)
            self.length += 1
