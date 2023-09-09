t = int(input())

for _ in range(t):
    n, b, h = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    previous_height = 0
    height_diffs = []
    for height in a:
        if previous_height > height:
            height_diffs.append(previous_height - height)
        previous_height = height + h

    ans = b * h * n / 2

    count = sum(diff * diff for diff in height_diffs)
    count = (count * b) / (2 * h)

    ans -= count

    print(f"{ans:.10f}".rstrip("0").rstrip("."))
