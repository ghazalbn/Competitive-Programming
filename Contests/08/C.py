def solve(n, c, d, a):
    # Initialize dp table
    dp = [[float('inf')] * n for _ in range(n)]

    # Initialize base cases
    dp[0][0] = 0 if a[0] == 1 else min(c, d)

    # Fill the dp table
    for i in range(1, n):
        for j in range(n):
            # Case 1: Skip the current element if it's already a valid number
            if a[i] == i + 1:
                dp[i][j] = dp[i-1][j]
            # Case 2: Remove the current element
            dp[i][j] = min(dp[i][j], dp[i-1][j] + c)
            # Case 3: Insert a new number x in any position of the already processed elements
            for k in range(j):
                dp[i][j] = min(dp[i][j], dp[i][k] + d)

            # If we have processed all n elements and we have a valid permutation, return the result
            if i == n - 1 and a[i] == n:
                return dp[i][j]

    # Return the minimum cost to get a valid permutation
    return min(dp[n-1][j] for j in range(n))


# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the input for each test case
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))

    # Solve the problem and print the result
    print(solve(n, c, d, a))
