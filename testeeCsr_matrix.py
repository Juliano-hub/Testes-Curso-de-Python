from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree


Matriz = csr_matrix([[1, 9, 11, 33],
                [2, 7, 2, 30],
                [3, 6, 0, 21],
                [4, 5, 9, 10]])

Tcsr = minimum_spanning_tree(Matriz)
Tcsr.toarray().astype(int)

for x in Tcsr:
    print(x)