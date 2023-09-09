t = int(input())

for i in range(t):
    n = int(input())
    powers = list(map(int, input().split()))

    stack = []
    total_power = 0

    for power in powers:
        if power == 0:
            if stack:
                bonus_power = stack.pop()
                total_power += bonus_power
        else:
            hero_power = power + (stack[-1] if stack else 0)
            total_power += hero_power
            stack.append(0)

    print(total_power)
