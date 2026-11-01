import math
import itertools

# Bài A19:
m = 4
n = 6
allMaps19 = list(itertools.product(range(n), repeat = m))
donAnh = [f for f in allMaps19 if len(set(f)) == m]
print("[A19a]: Số ánh xạ: Vét cạn:", len(allMaps19), "| Công thức:", n**m)
print("[A19b]: Số đơn ánh: Vét cạn:", len(donAnh), "| Công thức:", math.perm(n, m))

# Bài A20:
n = 6
allMaps20 = list(itertools.product(range(n), repeat = n))
songAnh = list(itertools.permutations(range(n)))

# (a): f(i) != i với mọi i (hoán vị vô trật tự - Dearrangement)
aMaps = [f for f in allMaps20 if all(f[i] != i for i in range(n))]
print("[A20a]: Hoán vị vô trật tự: Vét cạn:", len(aMaps))

# (b): song ánh và f(0) != 0
bMaps = [f for f in songAnh if f[0] != 0]
print("[A20b]: Số song ánh có f(0) != 0: Vét cạn:", len(bMaps), "| Công thức:", math.factorial(n) - math.factorial(n - 1))

# (c): f(0) != f(1) != f(2) != f(0)
cMaps = [f for f in allMaps20 if len(set(f[:3])) == 3]
print("[A20c]: Vét cạn:", len(cMaps), "| Công thức:", math.perm(n, 3) * (6**3))

# (d): song ánh và f(1) < f(2)
dMaps = [f for f in songAnh if f[1] < f[2]]
print("[A20d]: Vét cạn:", len(dMaps), "| Công thức:", math.factorial(n) // 2)