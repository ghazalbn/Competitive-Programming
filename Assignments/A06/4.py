# def dfs(node, visited, v):
#     cnt = 1
#     visited[node] = True
#     for i in v[node]:
#         if not visited[i]:
#             cnt += dfs(i, visited, v)
#     return cnt

# n, k = map(int, input().split())
# v = [[] for _ in range(n)]
# # visited = [False] * n

# for i in range(1, n):
#     a, b = map(int, input().split())
#     v[a - 1].append(b - 1)
#     v[b - 1].append(a - 1)

# ans = 0
# for i in range(n):
#     visited = [False] * n
#     visited[i] = True
#     cnt = dfs(i, visited, v)
#     ans += cnt

# print(ans)

def count_paths(node, remaining_steps, parent_node):
    if dp[node][remaining_steps] != -1:
        return dp[node][remaining_steps]
    elif remaining_steps == 0:
        return 1
    else:
        num_paths = 0
        for neighbor in tree[node]:
            if neighbor != parent_node:
                num_paths += count_paths(neighbor, remaining_steps-1, node)
        dp[node][remaining_steps] = num_paths
        return num_paths

def dfs(node, parent_node=0):
    parent[node] = parent_node
    for neighbor in tree[node]:
        if neighbor != parent_node:
            dfs(neighbor, node)


n, k = map(int, input().split())
tree = [[] for _ in range(n+1)]
dp = [[-1]*(k+1) for _ in range(n+1)]
parent = [0]*(n+1)

for i in range(n-1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)
    # parent[node2] = node1

dfs(1)
ans = 0
for node in range(1, n+1):
    a = count_paths(node, k, parent[node])
    b = 0
    for i in tree[node]:
        if i != parent[node]:
            for x in range(1, k):
                b += count_paths(i, x-1, node) * (count_paths(node, k-x, parent[node]) - count_paths(i, k-x-1, node))
    ans += a + 0.5*b
print(int(ans))
