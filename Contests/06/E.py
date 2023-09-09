from collections import deque

n = int(input())
labels = list(map(int, input().split()))

adj_list = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

def bfs(start):
    distances = [-1] * n
    distances[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances

good_vertices = []
for root in range(n):
    valid = True
    distances = bfs(root)
    for i in range(n):
        if labels[i] != distances[i]:
            valid = False
            break
    if valid:
        good_vertices.append(root+1)

print(len(good_vertices))
print(*good_vertices)
