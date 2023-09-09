t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    dist = list()
    for i in range(n-1):
        l = 0
        for j in dist:
            if s[:i] + s[i+2:] == s[:j] + s[j+2:]:
                l = 1
                break
        if not l:
            dist.append(i)
    print(len(dist))
