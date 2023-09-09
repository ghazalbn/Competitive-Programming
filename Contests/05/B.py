
#     a.sort()
#     for i in range(1, n):
#         while a[i] % a[i-1] == 0:
#             a[i] += 1

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    for i in range(n - 1):
        while a[i + 1] % a[i] == 0:
            if a[i] == 1 or a[i] == a[i + 1]:
                a[i] += 1
            else:
                a[i + 1] += 1
            if i > 0 and a[i] % a[i - 1] == 0:
                a[i] += 1

    print(*a)
