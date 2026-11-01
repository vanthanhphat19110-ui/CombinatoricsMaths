import math

def solutions_bruteforce(total, n, low = 0, high = None):
    if n == 1:
        if total >= low and (high is None or total <= high):
            return 1
        return 0
    
    count = 0
    upper = total if high is None else min(total, high)
    for x in range(low, upper + 1):
        count += solutions_bruteforce(total - x, n - 1, low, high)
    return count

r = 8
n = 4
print("x_i >= 0 (r = 8, n = 4): Vét cạn:", solutions_bruteforce(r, n, 0), "| Công thức:", math.comb(8 + 4 - 1, 4 - 1))
print("x_i >= 1 (r = 8, n = 4): Vét cạn:", solutions_bruteforce(r, n, 1), "| Công thức:", math.comb(8 - 1, 4 - 1))
print("x_i >= -2 (r = 8, n = 4): Vét cạn:", solutions_bruteforce(r, n, -2), "| Công thức:", math.comb(16 + 4 - 1, 4 - 1))