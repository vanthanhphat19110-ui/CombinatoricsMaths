def isValidA1(n):
    digits = str(n)
    return (n % 2 != 0) and (len(set(digits)) == 3)

# 01. Vét cạn.
countBruteForce = sum(1 for n in range(100, 1000) if isValidA1(n))

# 02. Công thức.
countFormula = 5 * 8 * 8

print(f"[B1]: Vét cạn: {countBruteForce} | Công thức: {countFormula}")