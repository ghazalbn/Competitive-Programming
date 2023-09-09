# from collections import deque

# def minimum_moves(n, graph):
#     queue = deque()
#     queue.append((0, 0)) 
#     visited = [False] * n
#     visited[0] = True

#     while queue:
#         node, moves = queue.popleft()

#         if node == n-1:
#             return moves

#         for adj_node in graph[node]:
#             if not visited[adj_node]:
#                 queue.append((adj_node, moves + 1))
#                 visited[adj_node] = True

#     return -1

import heapq

def minimum_moves(n, graph, start, end):
    distances = {node: float('inf') for node in range(n)}
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
p = [None] * 10
graph = [{} for _ in range(n)]
for i in range(n):
    si = int(s[i])
    if i > 0:
        graph[i][i - 1] = 1
    if i < n-1:
        graph[i][i + 1] = 1
    if p[si] is None:
        p[si] = i
    else:
        graph[p[si]][i] = 1
        graph[i][p[si]] = 0.5
        
result = minimum_moves(n, graph, 0, n - 1)
print(result)
