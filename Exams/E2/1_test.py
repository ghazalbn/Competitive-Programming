def rec(arr):
    if len(arr) < 2:
        return len(arr)
    
    current = arr[0]
    small = []
    big = []
    for ai in arr[1:]:
        if ai < current:
            small.append(ai)
        elif ai > current:
            big.append(ai)
    
    return 1 + rec(small) + rec(big)

n = int(input())
a = list(map(int, input().split()))
print(rec(a))

