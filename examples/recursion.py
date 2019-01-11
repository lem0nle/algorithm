from io import StringIO


def hanoi(s, t, m, k):
    """Recursion."""
    if k == 1:
        return [(s, t)]
    step1 = hanoi(s, m, t, k - 1)
    step2 = [(s, t)]
    step3 = hanoi(m, t, s, k - 1)
    return step1 + step2 + step3


class NQueens:
    def __init__(self, n):
        self.n = n
        self.r = []
        self.col = [0] * n
        self.ldiag = [0] * (2 * n - 1)
        self.rdiag = [0] * (2 * n - 1)

    def _isok(self, i, j):
        return not(self.col[j] or
                   self.ldiag[i + j] or
                   self.rdiag[i - j + self.n - 1])

    def _mark(self, i, j, flag):
        self.col[j] = flag
        self.ldiag[i + j] = flag
        self.rdiag[i - j + self.n - 1] = flag

    def solve(self, k=0):
        if k == self.n:
            yield NQueens.Solution(self.r[:])
        for j in range(self.n):
            if self._isok(k, j):
                self.r.append(j)
                self._mark(k, j, 1)
                yield from self.solve(k + 1)
                self.r.pop()
                self._mark(k, j, 0)

    def solve_one(self):
        try:
            return next(self.solve())
        except StopIteration:
            return None

    class Solution:
        def __init__(self, r):
            self.r = r

        def __str__(self):
            n = len(self.r)
            v = StringIO()
            for i in range(n):
                c = self.r[i]
                for j in range(n):
                    if j == c:
                        v.write('o ')
                    else:
                        v.write('. ')
                v.write('\n')
            return v.getvalue().strip()


if __name__ == '__main__':
    import sys
    print(len(list(NQueens(int(sys.argv[1])).solve())))
