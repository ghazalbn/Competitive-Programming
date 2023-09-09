MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

# Initialize DP table
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

# Fill in DP table diagonally
for d in range(1, n):
    for i in range(n-d):
        j = i + d
        dp[i][j] = dp[i+1][j]
        for k in range(i+1, j):
            if a[k] < a[i]:
                continue
            if a[k] > a[j]:
                break
            dp[i][j] += dp[i][k-1] * dp[k+1][j]
            dp[i][j] %= MOD

# Print answer
print(dp[0][n-1])
