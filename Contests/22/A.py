t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    suspicions = list(map(int, input().split()))

    differences = [abs(suspicions[i] - suspicions[i - 1]) for i in range(1, n)]
    differences.sort()
    sum_of_power = sum(differences[:n - k])
    print(sum_of_power)
