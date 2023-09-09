def longest_increasing_subsequence(a, n):
    lis = [a[0]]

    for i in range(1, n):
        if lis[-1] >= a[i]:
            l, r = 0, len(lis)-1
            while l <= r:
                m = int((l + r) / 2)
                if lis[m] < a[i]:
                    l = m + 1
                else:
                    r = m - 1
            lis[l] = a[i]
        else:
            lis.append(a[i])

    return len(lis)

n = int(input())
a = list(map(int, input().split()))
print(longest_increasing_subsequence(a, n))
