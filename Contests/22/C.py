t = int(input())

for _ in range(t):
    n = int(input())
    strengths = [0] + list(map(int, input().split()))
    max_strength = max(strengths)

    for i in range(1, n):
        xor_sum = strengths[i]
        for j in range(i + 1, min(n + 1, i + 257)):
            xor_sum ^= strengths[j]
            max_strength = max(max_strength, xor_sum)

    print(max_strength)
