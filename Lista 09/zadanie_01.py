import numpy

A = numpy.array(
    [
        [1, 2, 3, -2, -1],
        [3, 5, 5, -3, -9],
        [2, 3, 2, 0, -8],
        [2, 6, 7, -5, 1],
        [1, 2, 6, -4, -10],
    ],
    dtype=numpy.float,
)
B = numpy.array([6, 2, -5, 17, 12], dtype=numpy.float)
print(numpy.linalg.solve(A, B))
