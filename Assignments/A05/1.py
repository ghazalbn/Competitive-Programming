n = int(input())
a = [list(map(float, input().split())) for _ in range(n)]

num_masks = 1 << n
dp = [0] * num_masks

initial_mask = (1 << n) - 1
dp[initial_mask] = 1

for mask in range(initial_mask - 1, 0, -1):
    num_selected = len([i for i in range(n) if mask & (1 << i)])
    num_pairs = num_selected * (num_selected + 1) // 2
    for j in range(n):
        if not mask & (1 << j):
            for k in range(n):
                if mask & (1 << k):
                    dp[mask] += dp[mask | (1 << j)] * a[k][j] / num_pairs

print(" ".join([f"{dp[1<<i]:.6f}" for i in range(n)]))
