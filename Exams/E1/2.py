n = int(input())
a = list(map(int, input().split()))

count = [[1] * (n) for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[i] == a[j]:
                # print(i, j)
            count[i][j] = count[i + 1][j - 1] + 2
            # elif i > j:
        elif count[i + 1][j] > count[i][j - 1]:
            count[i][j] = count[i + 1][j]
        else:
            count[i][j] = count[i][j - 1]
print(count[0][n - 1])