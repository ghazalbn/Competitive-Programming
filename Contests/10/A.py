for _ in range(int(input())):
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_interest = -1
    max_index = -1

    for i in range(n):
        if a[i] + i <= t:
            if b[i] > max_interest:
                max_interest = b[i]
                max_index = i + 1

    print(max_index)
