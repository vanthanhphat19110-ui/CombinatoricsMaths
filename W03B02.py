import math
import itertools

def countSurjective(m: int, n: int) -> int:
    sum = 0
    for k in range(0, n + 1):
        sum += ((-1) **k) * math.comb(n, k) * ((n - k) ** m)
    return sum


# Bài A8a:
m = 6
n = 4
allMaps_A8a = list(itertools.product(range(n), repeat = m))
surjective_A8a = [f for f in allMaps_A8a if len(set(f)) == n]
print("[A8a]: Vét cạn:", len(surjective_A8a), "| Công thức:", countSurjective(m, n))

# Bài A8b:
m = 7
n = 4
allMaps_A8b = list(itertools.product(range(n), repeat = m))
surjective_A8b = [f for f in allMaps_A8b if len(set(f)) == n]
print("[A8b]: Vét cạn:", len(surjective_A8b), "| Công thức:", countSurjective(m, n))

# Bài A9:
m = 6
n = 3
allMaps_A9 = list(itertools.product(range(n), repeat = m))
surjective_A9 = [f for f in allMaps_A9 if len(set(f)) == n]
print("[A9]: Không đánh STT: Vét cạn:", len(surjective_A9), "| Công thức:", countSurjective(m, n))
print("[A9]: Có tên: Vét cạn:", len(surjective_A9) // math.factorial(n), "| Công thức:", countSurjective(m, n) // math.factorial(n))