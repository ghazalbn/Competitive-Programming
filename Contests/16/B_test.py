t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    min_cost = 1
    current = s[0]
    consecutive_count = 0
    for char in s:
        if char == current:
            consecutive_count += 1
        else:
            min_cost = max(min_cost, consecutive_count)
            consecutive_count = 1
            current = char
    min_cost = max(min_cost, consecutive_count)
    print(min_cost + 1)
