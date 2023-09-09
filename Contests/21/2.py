def snake_beads(n, m):
    snake_table = [[0] * m for _ in range(n)]
    row, col = 0, 0
    direction = 1

    for bead in range(1, n * m + 1):
        snake_table[row][col] = bead

        col += direction
        if col == m and direction == 1:
            col = m - 1
            row += 1
            direction = -1
        elif col == -1 and direction == -1:
            col = 0
            row += 1
            direction = 1

    return snake_table

n, m = map(int, input().split())
table = snake_beads(n, m)
for row in table:
    print(*row)
