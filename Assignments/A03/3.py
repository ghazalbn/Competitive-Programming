n = int(input())

def greatest_factor(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return int(num / i)
    return 1

gf = greatest_factor(n)

print(gf, n - gf)
