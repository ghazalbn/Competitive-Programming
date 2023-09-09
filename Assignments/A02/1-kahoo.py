t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    step = 0
    a.sort()

    for i in range(1, n):
        mn, mx = a[0], a[i]
        new = mn * 2 - 1
        if mx <= new:
            continue
        num = int(mx / new)
        if mx % new:    
            step += 1         
        step += num - 1

    print(step)


# while(True):
#     n = len(a)
#     mx, mn = a[n - 1], a[0]

#     if mx < mn * 2:
#         break

#     new = mn * 2 - 1
#     num = int(mx / new)
#     a = a[: -1]

#     if mx % new:
#         a.append(mx % new)      
#         step += 1         

#     a.extend([new] * num)
#     a.sort()
#     step += num - 1
