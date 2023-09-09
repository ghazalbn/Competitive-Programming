t = int(input())

for _ in range(t):
    n = int(input())
    vampires = list(map(int, input().split()))

    max_strength = 1
    while max_strength <= 1e9:
        max_strength *= 2
    max_strength -= 1

    min_strength = max_strength
    for i in range(n):
        min_strength &= vampires[i]

    groups = 0
    current_strength = max_strength

    for i in range(n):
        current_strength &= vampires[i]
        if current_strength == 0:
            groups += 1
            current_strength = max_strength

    groups += min_strength > 0
    print(groups)
