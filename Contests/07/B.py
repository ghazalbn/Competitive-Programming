def min_vaccine_packs(n, k, d, w, t):
    l = 1
    r = 2
    packs = 1
    while r < n:
        while r < n-1 and t[r+1] - t[l] <= w:
            r += 1
        if t[r] - t[l-1] <= w:
            r += 1
        else:
            packs += 1
        l = r + 1
        r = l + k - 2
    return packs

tests = int(input())
for _ in range(tests):
    n, k, d, w = map(int, input().split())
    t = list(map(int, input().split()))
    packs = 0
    tul = d + w
    l = 0
    r = 0
    while l < n:
        while r - l + 1 < k and r < n - 1:
            if t[r + 1] - t[l] <= tul:
                r += 1
            else:
                break
        l = r + 1
        r = l
        packs += 1
    
    print(packs)