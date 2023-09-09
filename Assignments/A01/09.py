n = int(input())
a = list(map(int, input().split()))

for ai in a:
    print("*" * (ai if ai <= 3 else 1))
