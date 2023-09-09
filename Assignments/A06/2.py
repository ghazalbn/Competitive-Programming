MOD = 10**9 + 7

def dfs(dp, n, l):
    if dp[l][n]:
        return dp[l][n]
    if l == 1 or n == 1:
        return n
    ret = 0
    for i in range(1, n + 1):
        ret += dfs(dp, i, l - 1) % MOD
        ret %= MOD
    dp[l][n] = ret
    return ret

n, m = map(int, input().split())
dp = [[0]*(n+1) for _ in range(2*m+1)]
print(dfs(dp, n, 2 * m))
