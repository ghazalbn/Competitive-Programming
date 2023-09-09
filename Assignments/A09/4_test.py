import heapq

def dijkstra(root, graph, n, k):
    result = n
    distances = [float('inf') for node in range(n + 1)]
    if distances[root] >= k:
        result -= 1
    distances[root] = 0
    s = [(0, root)]
    heapq.heapify(s)
    
    while s:
        d, city = heapq.heappop(s)
        
        if distances[city] < d:
            continue
        
        for neighbor, road_length in graph[city].items():
            if distances[neighbor] > d + road_length and d + road_length < k:
                if distances[neighbor] >= k:
                    result -= 1
                distances[neighbor] = d + road_length
                heapq.heappush(s, (distances[neighbor], neighbor))
    return result



n, m, t, k = map(int, input().split())

graph = [{} for _ in range(n + 1)]

for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v][u] = w
    graph[u][v] = w

for _ in range(t):
    a = int(input())
    result = dijkstra(a, graph, n, k)
    print(result)
