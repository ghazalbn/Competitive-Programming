MOD = 7 + 10**9

def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return result

def inverse(n):
    return power(n, MOD - 2)

n, k = map(int, input().split())
numerator = 1
denominator = 1

for i in range(1, k+1):
    numerator = (numerator * (n - k + i)) % MOD
    denominator = (denominator * i) % MOD

result = (numerator * inverse(denominator)) % MOD
print(result)
