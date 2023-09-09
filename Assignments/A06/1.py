import math
# import sys
# sys.setrecursionlimit(10**7)

def dfs(u, parent):
    amount = 0
    for v, state in town[u]:
        if v != parent:
            amount += (not state) + dfs(v, u)
    return amount

def dfs_all(u, parent):
    for v, state in town[u]:
        if v != parent:
            dp[v] = dp[u] + (1 if state else -1)
            dfs_all(v, u)

n = int(input())
town = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for i in range(n-1):
    s, t = map(int, input().split())
    town[s].append((t, 1))
    town[t].append((s, 0))

dp[1] = dfs(1, 0)
dfs_all(1, 0)

min_road = min(dp[1:])

print(min_road)
print(*[i for i in range(1, n+1) if dp[i] == min_road], sep=" ")