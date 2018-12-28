from random import randint


class RandomQueue:
    def __init__(self):
        self.queue = []
        self.size = len(self.queue)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        queue = self.queue
        ind = randint(0, self.size - 1)
        queue[-1], queue[ind] = queue[ind], queue[-1]
        return self.queue.pop()
