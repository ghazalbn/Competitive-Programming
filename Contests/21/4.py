def maximum_satisfaction(t, countries):
    results = []
    for country in countries:
        n, m = country[0]
        cities = country[1:]

        # Initialize the dynamic programming table
        dp = [[0] * m for _ in range(n)]

        # Fill the base case
        dp[0][0] = cities[0][0]

        # Fill the first row
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + cities[0][j]

        # Fill the first column
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + cities[i][0]

        # Fill the remaining cells
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cities[i][j]

        # Add the maximum satisfaction for this country to the results
        results.append(dp[n-1][m-1])

    return results

# Get input from the user
t = int(input())
countries = []
for _ in range(t):
    n, m = map(int, input().split())
    cities = []
    for _ in range(n):
        row = list(map(int, input().split()))
        cities.append(row)
    country = [(n, m)] + cities
    countries.append(country)

# Calculate maximum satisfaction
results = maximum_satisfaction(t, countries)

# Print the results
for result in results:
    print(result)
