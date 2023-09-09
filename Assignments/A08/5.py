import heapq

n, m = map(int, input().split())
strength = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(m):
    v, u = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

min_additional_power = [0] * n
for start_country in range(n):
    visited = [False] * n
    visited[start_country] = True

    heap = [(strength[start_country], start_country)]
    strn = 0
    while heap:
        d, v = heapq.heappop(heap)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(heap, (strength[neighbor], neighbor))
                visited[neighbor] = True

        if v == start_country or strn > d:
            strn += d
            continue
        new = d - strn + 1
        min_additional_power[start_country] += new
        strn += new + d

print(*min_additional_power)