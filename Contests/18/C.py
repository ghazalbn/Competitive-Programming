t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = n
    prev = a[0]

    if n == 1 or (n == 2 and a[1] == prev):
        print(1)
    elif n == 2:
        print(2)
    else:
        curr = a[1]
        for i in range(2, n):
            if (prev <= curr and curr <= a[i]) or (prev >= curr and curr >= a[i]):
                curr = a[i]
                res -= 1
            else:
                prev = curr
                curr = a[i]

        if prev == curr:
            print(res - 1)
        else:
            print(res)
