n = int(input())
board = [input() for _ in range(n)]

def is_ok(board, row, col):
    if board[row][col] in ['#', 'A']:
        return False
    bad = [(2, 1), (2, -1), (-2, 1), (-2, -1), (2, 1),
    (1, 2), (-1, 2), (1, -2), (-1, -2)]
    for i, j in bad:
        if row + i > -1 and row + i < n  and col + j > -1 and col + j < n \
            and board[row + i][col + j] == 'A':
            return False
    return True

for row in range(n):
    for col in range(n):
        if is_ok(board, row, col):
            board[row] = board[row][:col] + 'A' + board[row][col + 1:]

print(*board, sep='\n')

