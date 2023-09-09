t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for ai in a:
        print(n - ai + 1, end=' ')
    print()