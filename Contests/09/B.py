for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_tag = list(map(int, input().split()))

    l = 0
    while l < n - 1 and a[l] == a_tag[l]:
        l += 1
    r = n - 1
    while r > 0 and a[r] == a_tag[r]:
        r -= 1

    # min_a = min(a[l:r+1])
    # max_a = max(a[l:r+1])

    left = l
    # if left >= 0 and left < n - 1 and a_tag[left - 1] < a_tag[left]:
    #     left -= 1
    while left > 0 and left < n and a_tag[left - 1] <= a_tag[left]:
        left -= 1
    right = r
    # if right < n and right > 0 and a_tag[right] > a_tag[right - 1]:
    #     right += 1
    while right < n - 1 and right >= 0 and a_tag[right + 1] >= a_tag[right]:
        right += 1

    
    print(left+1, right+1)
