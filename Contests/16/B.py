t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    i = 0
    min_cost = 1
    pre = 0
    while i < n:
        current = s[i]
        j = i
        while j < n and s[j] == current:
            if pre > 0:
                pre -= 1
            else:
                min_cost += 1
            j += 1
        pre = j - i
        i = j

    print(min_cost)
