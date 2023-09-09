t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    m = int(input())
    l = input()
    r = input()

    positions = [[] for _ in range(10)]
    indices = [0] * 10

    for i in range(n):
        positions[int(s[i])].append(i)

    current_position = 0
    for i in range(m):
        for j in range(10):
            while indices[j] < len(positions[j]) and positions[j][indices[j]] < current_position:
                indices[j] += 1

        max_position = current_position
        for j in range(int(l[i]), int(r[i]) + 1):
            if indices[j] >= len(positions[j]):
                max_position = n
            else:
                max_position = max(max_position, positions[j][indices[j]])

        current_position = max_position + 1

    print("YES" if current_position >= n + 1 else "NO")