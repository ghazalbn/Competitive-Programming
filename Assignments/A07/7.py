import sys
sys.setrecursionlimit(10**9)

def dfs(adj, v, visited):
    visited[v] = 1
    for u in adj[v]:
        if visited[u] == 0:
            if not dfs(adj, u, visited):
                return False
        elif visited[u] == 2:
            return False
    visited[v] = 2
    return True

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
flag = False
for i in range(n):
    visited = [0 for _ in range(n)]
    if not dfs(adj, i, visited):
        flag = True
        break
    
print("No" if flag else "Yes")