n, x = map(int, input().split())
s = input()

for i in range(n):
    x = max(0, x + (1 if s[i] == 'o' else -1))

print(x)