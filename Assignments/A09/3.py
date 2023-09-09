import heapq

def minimum_moves(n, graph, start, end):
    distances = {node: float('inf') for node in range(n + 10)}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return current_distance

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1

n = int(input())
s = input()
graph = [{} for _ in range(n + 10)]
for i in range(n):
    si = int(s[i])
    if i > 0:
        graph[i + 10][i + 9] = 1
    if i < n-1:
        graph[i+10][i+11] = 1
    graph[si][i+10] = 0.5
    graph[i+10][si] = 0.5

result = minimum_moves(n, graph, 10, n + 9)
print(int(result))
