t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    f = "NO"
    for i in range(n):
        if a[i] <= i + 1:
            f = "YES"
    print(f)
