# import numpy as np
import math

def max_profit(mask, last, count):
    if count > n:
        return -math.inf

    if count == m:
        return 0

    best = dp[mask][last]
    if best == -1:
        best = 0
        for i in range(n):
            if (mask & (1 << i)) == 0:
                best = max(best, max_profit(mask | (1 << i), i, count + 1) + a[i] + b[last][i])

        dp[mask][last] = best
    return best


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = [[0]*n for i in range(n)]
# b = np.zeros((n, n), dtype=int)

for i in range(k):
    x, y, c = map(int, input().split())
    b[x - 1][y - 1] = c

dp = [[-1]*n for i in range(1 << n)]
# dp = np.full((1 << n, n), -1, dtype=np.int64)

profit = 0
for i in range(n):
    profit = max(profit, max_profit((1 << i), i, 1) + a[i])

print(profit)
