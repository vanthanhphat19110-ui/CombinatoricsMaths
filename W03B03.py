import itertools
import sympy
from sympy.functions.combinatorial.numbers import stirling

for n in range (1, 8 + 1):
    bruteForceDearrangement = sum(1 for perms in itertools.permutations(range(n)) if all(perms[i] != i for i in range(n)))
    formulaDearrangement = sympy.subfactorial(n)
    print("Dearrangement: Vét cạn:", bruteForceDearrangement, "| Công thức:", formulaDearrangement)

m = 6
n = 3
print("Stirling type 2:", stirling(m, n, kind = 2))