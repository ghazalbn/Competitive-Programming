for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    for num in a:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    ans = max(max1 * max2, min1 * min2)
    print(0 if ans == 0 or ans == -0 else ans)
