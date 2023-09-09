t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    prefix_sum_left = [0] * (2 * k + 1)
    prefix_sum_right = [0] * (2 * k + 1)
    prefix_sum_left[1] = a[0] + a[1]
    prefix_sum_right[1] = a[n - 1]
    for i in range(1, k):
        prefix_sum_left[i + 1] = prefix_sum_left[i] + a[2 * i] + a[2 * i + 1]
        prefix_sum_right[i + 1] = prefix_sum_right[i] + a[n - i - 1]
        
    minimum_sum_diff = float('inf')
    for i in range(k + 1):
        minimum_sum_diff = min(minimum_sum_diff, prefix_sum_left[i] + prefix_sum_right[k - i])
    print(sum(a) - minimum_sum_diff)
