n, k = map(int, input().split())
sizes = list(map(int, input().split()))

dp = [[float('inf')] * k for _ in range(k)]
for i in range(k):
    dp[i][i] = 0

for sz in range(2, k+1):
    for l in range(k-sz+1):
        r = l + sz - 1
        size_l_r = sum(sizes[l:r+1])
        for i in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][i] + dp[i+1][r] + size_l_r)

print(dp[0][k-1])


# time = 0
# while len(sizes) > 1:
#     min_time, min_i = sizes[0] + sizes[1], 0
#     for i in range(1, len(sizes) - 1):
#         t = sizes[i] + sizes[i + 1]
#         if t < min_time:
#             min_time, min_i = t, i
#     sizes = sizes[:min_i] + [min_time] + sizes[min_i + 2:]
#     time += min_time
# print(time)