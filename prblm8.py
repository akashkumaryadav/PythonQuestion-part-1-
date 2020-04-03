import numpy as np


class EqMat():
    m = 0
    n = 0

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = np.array(range(m*n), dtype=float).reshape(m, n)

    def readarray(self):
        for r in range(self.m):
            for c in range(self.n):
                self.matrix[r][c] = float(
                    input(f"enter the ({r},{c}) element of matrix"))

    def check(self, anotherMatrix):
        print(np.array_equal(self.matrix, anotherMatrix.matrix))

    def diplay(self):
        print(self.matrix)


e = EqMat(2, 2)
e.readarray()
e.diplay()
e1 = EqMat(2, 2)
e1.readarray()
e1.diplay()
e.check(e1)
