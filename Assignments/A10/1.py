n, q = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    interval_sum = prefix_sum[r] - prefix_sum[l - 1]
    print(interval_sum)
