n, m = map(int, input().split())
mat = [[0]*n for i in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    mat[u - 1][v - 1] = 1
    mat[v - 1][u - 1] = 1
print('\n'.join([''.join(map(str, row)) for row in mat]))
