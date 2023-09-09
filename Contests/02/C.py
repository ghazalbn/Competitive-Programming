t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)
    sorted_s = sorted(s, reverse=True)
    t = sorted_s[0]
    for i in range(1, n):
        if i % 2 == 1:
            t = sorted_s[i] + t
        else:
            t = t + sorted_s[i]
    t_reverse = t[::-1]
    tmax = max(t, t_reverse)
    print(tmax)
