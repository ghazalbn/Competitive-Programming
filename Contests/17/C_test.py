from collections import deque

def find_parent(adj, visited, parent, node):
    visited[node] = 1
    stack = deque([node])

    while stack:
        curr = stack.pop()
        for neighbor in adj[curr]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                parent[neighbor] = curr
                stack.append(neighbor)

def dfs(adj, s, dp, loc, visited):
    visited[s] = 1
    stack = deque([(s, dp[s])])

    while stack:
        curr, dist = stack.pop()
        for neighbor in adj[curr]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                dp[neighbor] = dist + 1 if loc[curr] > loc[neighbor] else dist
                stack.append((neighbor, dp[neighbor]))

t = int(input())

for _ in range(t):
    n = int(input())
    adj = [[] for _ in range(n)]
    loc = [0] * n
    edges = []
    parent = [-1] * n

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
        edges.append((u-1, v-1))

    visited = [0] * n
    find_parent(adj, visited, parent, 0)

    for i in range(len(edges)):
        if edges[i][0] == parent[edges[i][1]]:
            loc[edges[i][1]] = i
        else:
            loc[edges[i][0]] = i

    dp = [0] * n
    visited = [0] * n
    dfs(adj, 0, dp, loc, visited)

    print(max(dp) + 1)
