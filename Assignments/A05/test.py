MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]

# for i in range(n-1):
#     if a[i] > a[i+1]:
#         dp[i][i+1] = 1
#         dp[i][i-1] = 1

# for i in range(1, n):
#     dp[i][i-1] = 1

# for sz in range(4, n+1, 2):
#     for l in range(n-sz+1):
#         r = l + sz - 1
#         for i in range(l + 1, r + 1, 2):
#             if a[l] > a[i]:
#                 dp[l][r] = (dp[l][r] + dp[l+1][i-1]*dp[i+1][r]) % MOD
#         f = (r-l+1)*(r-l) // 2
#         dp[l][r] *= f        

# print(dp[0][n-1])



# Functions
# def make_pow(x, y, MOD):
#     if y == 0:
#         return 1
#     elif y % 2 == 1:
#         return x * make_pow((x * x) % MOD, y // 2, MOD) % MOD
#     else:
#         return make_pow((x * x) % MOD, y // 2, MOD) % MOD

def FUNC(p, q):
    q = min(q, p - q)
    res = 1
    tmp = 1
    for i in range(q):
        res = (res * (p - i)) % MOD
    for j in range(2, q + 1):
        tmp = (tmp * j) % MOD
    # tmp = make_pow(tmp, MOD - 2, MOD)
    tmp = pow(tmp, MOD - 2, MOD)
    return (res * tmp) % MOD


for i in range(n):
    dp[i][i] = 1

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        for q in range(i + 1, j + 1):
            if a[i] > a[q]:
                n = dp[i + 1][q - 1]
                k = dp[q + 1][j]
                if (q - i - 1) // 2 == 0 and (j - q) // 2 == 0:
                    dp[i][j] = 1
                elif (q - i - 1) // 2 == 0 and k:
                    dp[i][j] = (dp[i][j] + ((((j - q) // 2) + 1) * k) % MOD) % MOD
                elif (j - q) // 2 == 0 and n:
                    dp[i][j] = (dp[i][j] + dp[i + 1][q - 1]) % MOD
                else:
                    dp[i][j] = (dp[i][j] + (((FUNC(((q - i - 1) // 2) + ((j - q) // 2) + 1, (j - q) // 2) * n) % MOD) * k) % MOD) % MOD

print(dp[0][n - 1])

