t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cold = list(map(int, input().split()))
    hot = list(map(int, input().split()))

    counts = [a.count(i + 1) for i in range(k)]
    # s = np.sum(np.add(np.multiply(cold, np.int64(counts > 0)), np.multiply(np.maximum(0, counts - 1), hot)))
    time = 0
    for i in range(k):
        if counts[i]:
            time += cold[i] + (counts[i] - 1) * hot[i]

    print(time)

# from sys import stdin, stdout

# def solve(n, k, a, cold, hot):
#     # initialize the minimum time taken for the first program
#     dp = [cold[a[0]-1]]*k
    
#     # keep track of the last program run on each CPU
#     last_prog = [-1]*k
    
#     # iterate over the remaining programs
#     for i in range(1, n):
#         # initialize the minimum time taken for this program
#         cur_dp = [float('inf')]*k
        
#         # iterate over the CPUs
#         for j in range(k):
#             # check the minimum time taken to run the program on the first CPU
#             if last_prog[j] != a[i]-1:
#                 cur_dp[j] = min(cur_dp[j], dp[j]+cold[a[i]-1])
#             else:
#                 cur_dp[j] = min(cur_dp[j], dp[j]+hot[a[i]-1])
            
#             # check the minimum time taken to run the program on the second CPU
#             if last_prog[1-j] != a[i]-1:
#                 cur_dp[j] = min(cur_dp[j], dp[1-j]+cold[a[i]-1])
#             else:
#                 cur_dp[j] = min(cur_dp[j], dp[1-j]+hot[a[i]-1])
        
#         # update the minimum time taken and the last program run on each CPU
#         dp = cur_dp
#         last_prog = [a[i]-1]*k
    
#     # return the minimum time taken to run the last program on either CPU
#     return min(dp)

# t = int(stdin.readline())

# for _ in range(t):
#     n, k = map(int, stdin.readline().split())
#     a = list(map(int, stdin.readline().split()))
#     cold = list(map(int, stdin.readline().split()))
#     hot = list(map(int, stdin.readline().split()))
#     stdout.write(str(solve(n, k, a, cold, hot)) + "\n")

