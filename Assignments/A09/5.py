import heapq

def min_cost_to_reach_destination(n, m, k, sx, sy, ex, ey, table, embassies):
    distance = [[float('inf')] * m for _ in range(n)]
    passport = [[False] * m for _ in range(n)]

    distance[sx][sy] = 0
    queue = [(0, sx, sy)]

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == ex and y == ey:
            return cost

        if distance[x][y] < cost:
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            new_cost = cost

            if table[nx][ny] > 0:
                if not passport[nx][ny]:
                    if (nx, ny) in embassies and embassies[(nx, ny)] == table[nx][ny]:
                        new_cost += 0  # No cost to enter a country if passing through a free zone with an embassy
                        passport[nx][ny] = True
                    else:
                        new_cost += 1  # Entry fee for reaching a country
                        passport[nx][ny] = True
            elif table[nx][ny] == 0:
                new_cost += 0  # No cost to reach a free zone

            if new_cost < distance[nx][ny]:
                distance[nx][ny] = new_cost
                heapq.heappush(queue, (new_cost, nx, ny))

    return -1

# Read input values
n, m, k = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())

# Read the table
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

# Read embassies
embassies = {}
for _ in range(k):
    x, y, p = map(int, input().split())
    embassies[(x, y)] = p

# Call the function to get the minimum cost
result = min_cost_to_reach_destination(n, m, k, sx-1, sy-1, ex-1, ey-1, table, embassies)

# Print the result
print(result)
