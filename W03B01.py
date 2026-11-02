import math

# Bài A1:
N_A1 = 1000
countBruteForce_A1 = sum(1 for k in range(1, N_A1 + 1) if k % 3 == 0 or k % 5 == 0)
countFormula_A1 = (N_A1 // 3) + (N_A1 // 5) - (N_A1 // math.lcm(3, 5))
print("[A1]: Vét cạn:", countBruteForce_A1, "| Công thức:", countFormula_A1)

# Bài A3:
N_A3 = 800
countBruteForce_A3 = sum(1 for k in range(1, N_A3 + 1) if k % 6 == 0 or k % 10 == 0 or k % 15 == 0)
countFormula_A3 = (N_A3 // 6) + (N_A3 // 10) + (N_A3 // 15) - (N_A3 // math.lcm(6, 10)) - (N_A3 // math.lcm(10, 15)) - (N_A3 // math.lcm(15, 6)) + (N_A3 // math.lcm(6, 10, 15))
print("[A3]: Vét cạn:", countBruteForce_A3, "| Công thức:", countFormula_A3)