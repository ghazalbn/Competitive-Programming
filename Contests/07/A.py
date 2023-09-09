t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    row_steps = abs(a)
    col_steps = abs(b)
    if abs(row_steps - col_steps) < 2:
        print(row_steps+col_steps)
    else:
        print(max(row_steps, col_steps)*2-1)
