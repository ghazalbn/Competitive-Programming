def dfs(grid, visited, row, col, volume):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or visited[row][col] or grid[row][col] == 0:
        return volume
    visited[row][col] = True
    volume += grid[row][col]
    volume = dfs(grid, visited, row-1, col, volume)
    volume = dfs(grid, visited, row+1, col, volume)
    volume = dfs(grid, visited, row, col-1, volume)
    volume = dfs(grid, visited, row, col+1, volume)
    return volume

def find_largest_volume(grid):
    largest_volume = 0
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not visited[row][col] and grid[row][col] > 0:
                volume = dfs(grid, visited, row, col, 0)
                largest_volume = max(largest_volume, volume)
    return largest_volume

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # if m == 0 or n == 0:
    #     print(0)
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(find_largest_volume(grid))


def find_largest_volume(grid):
    largest_volume = 0
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    stack = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not visited[row][col] and grid[row][col] > 0:
                volume = 0
                stack.append((row, col))
                visited[row][col] = True
                while stack:
                    r, c = stack.pop()
                    volume += grid[r][c]
                    if r > 0 and not visited[r-1][c] and grid[r-1][c] > 0:
                        stack.append((r-1, c))
                        visited[r-1][c] = True
                    if r < len(grid)-1 and not visited[r+1][c] and grid[r+1][c] > 0:
                        stack.append((r+1, c))
                        visited[r+1][c] = True
                    if c > 0 and not visited[r][c-1] and grid[r][c-1] > 0:
                        stack.append((r, c-1))
                        visited[r][c-1] = True
                    if c < len(grid[0])-1 and not visited[r][c+1] and grid[r][c+1] > 0:
                        stack.append((r, c+1))
                        visited[r][c+1] = True
                largest_volume = max(largest_volume, volume)
    return largest_volume

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(find_largest_volume(grid))
