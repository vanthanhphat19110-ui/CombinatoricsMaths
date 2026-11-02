import itertools
import math

# Bài A6:
targetSum = 20
limits_A6 = [8, 8, 8, 8]
length_A6 = len(limits_A6)
ranges = [range(b + 1) for b in limits_A6]
countBruteForce_A6 = sum (1 for x in itertools.product(*ranges) if sum(x) == targetSum)