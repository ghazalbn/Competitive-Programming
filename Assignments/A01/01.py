n = int(input())
a, b, count = 0, 0, 0
for i in range(n):
    b = int(input())
    count += i != 0 and a != b
    a = b
print(count)
