import itertools
import math

# Bài A2:
s = "abcdef"

# (a): tùy ý --> product
p_a = list(itertools.product(s, repeat = 3))
print("[A2a]: Vét cạn:", len(p_a), "| Công thức:", 6**3)

# (b): đôi một khác nhau --> permutations
p_b = list(itertools.permutations(s, 3))
print("[A2b]: Vét cạn:", len(p_b), "| Công thức:", math.perm(6, 3))

# (c): đôi một khác nhau và có chứa "f"
p_c = [c for c in p_b if 'f' in c]
print("[A2c]: Vét cạn:", len(p_c), "| Công thức:", 3 * math.perm(5, 2))

# Bài A4:
binaryDigits = "01"
bits = list(itertools.product(binaryDigits, repeat = 8))
bitsWith3Zeroes = [b for b in bits if b.count('0') == 3]
print("[A4]: Số bits: Vét cạn:", len(bits), "| Công thức:", 2**8)
print("[A4]: Số bits có 3 số 0: Vét cạn:", len(bitsWith3Zeroes), "| Công thức:", math.comb(8, 3))

# Bài A13:
fruits = [1, 2, 3, 4, 5]
choose = list(itertools.combinations_with_replacement(fruits, 12))
print("[A13]: Vét cạn:", len(choose), "| Công thức:", math.comb(12 + 5 - 1, 5 - 1))