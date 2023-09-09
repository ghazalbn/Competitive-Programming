t = int(input())
for _ in range(t):
    n = int(input())
    plan = list(map(int, input().split()))
    extra = 0
    aviaries = 0
    ones = 0

    for day in plan:
        if day == 2:
            need = int(ones / 2) + 1
            extra = max(0, aviaries - need)

        elif day == 1:
            ones += 1
            if extra > 0:
                extra -= 1
            else:
                aviaries += 1

    print(aviaries)
