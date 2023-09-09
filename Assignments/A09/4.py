import heapq

def dijkstra(start, result):
    if distances[start] >= k:
        result -= 1
    distances[start] = 0

    pqueue = [(0, start)]
    
    while pqueue:
        d, city = heapq.heappop(pqueue)
        
        if distances[city] < d:
            continue
        
        for neighbor, road_cost in graph[city].items():
            distance = d + road_cost
            if distances[neighbor] > distance and distance < k:
                if distances[neighbor] >= k:
                    result -= 1
                distances[neighbor] = distance
                heapq.heappush(pqueue, (distance, neighbor))
    return result

n, m, t, k = map(int, input().split())

graph = [{} for _ in range(n + 1)]
distances = [float('inf') for node in range(n + 1)]
result = n

for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v][u] = w
    graph[u][v] = w

for _ in range(t):
    a = int(input())
    result = dijkstra(a, result)
    print(result)
