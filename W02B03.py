import math
from collections import Counter

def perm_multiset(word):
    n = len(word)
    counts = Counter(word)
    denom = 1
    for r in counts.values():
        denom *= math.factorial(r)
    return math.factorial(n) // denom

print("VISITING:",  perm_multiset("VISITING"))
print("GOOD:", perm_multiset("GOOD"))
print("ALGORITHM:", perm_multiset("ALGORITHM"))

# Bài A11a:
trees = "P" * 6 + "B" * 5 + "X" * 4
print("[A11a]:", perm_multiset(trees))