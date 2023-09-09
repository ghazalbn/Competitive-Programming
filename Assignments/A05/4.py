n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    s, k = map(int, input().split())
    result, end = 0, (n - s) // k
    for i in range(end + 1):
        result += a[i * k + s - 1]
    print(result)


# n = int(input())
# a = list(map(int, input().split()))

# dp = [[0]*(n+1) for i in range(n+1)]
# for k in range(1, n+1):
#     for s in range(n, 0, -1):
#         if s + k > n:
#             dp[s][k] = a[s-1]
#         else:
#             dp[s][k] = a[s-1] + dp[s+k][k]

# q = int(input())
# for i in range(q):
#     s, k = map(int, input().split())
#     print(dp[s][k])


n = int(input())
a = list(map(int, input().split()))

dp = [0]*(n+1)
for s in range(n, 0, -1):
    dp[s] = a[s-1] + dp[s+1] if s < n else a[s-1]

q = int(input())
for i in range(q):
    s, k = map(int, input().split())
    res = 0
    if k == 1:
        res = dp[s]
    else:
        m = (n - s) // k + 1
        res = dp[s] - dp[min(s+k*m, n+1)] + a[s+k*(m-1)]
    print(res)




