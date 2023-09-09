n = int(input())
fibo = [1,2]

for i in range(2, 100):
    a = fibo[i-2] + fibo[i-1]
    fibo.append(a)

for i in range(1, n + 1):
    a = fibo.count(i)
    print('+' if a == 1 else '-', end = "")