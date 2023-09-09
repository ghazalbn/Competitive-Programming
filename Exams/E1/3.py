import numpy as np

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

# def divisor(n):
#     divisors = [1] * (n + 1)
#     for j in range(i, n + 1, i):
#         divisors[j] += 1
#     a = n // i
#     summ += i * int((a * (a + 1)) / (2))

def prime_factor(a, b):
    is_prime = [True] * (a + 1)
    is_prime[0] = is_prime[1] = False
    factors = [0] * (b + 1)
    for i in range(2, a + 1):
        if is_prime[i]:
            factors[i] = 1
            for j in range(2 * i, a + 1, i):
                is_prime[j] = False
                factors[j] += 1
    return factors


a, b = map(int, input().split())
# factors_a = prime_factor(a, b)
# factors_b = prime_factor(b, b)
# for i in range(2, a + 1):
#     factors_b[i]  -=  prime_factor(i, b)[i]
# divisors = 1
# for f in factors_b:
#     divisors = (divisors * (f + 1)) % MOD

# numerator = 1
# denominator = 1
# s = 1

# for i in range(1, a+1):
#     denominator = (denominator * i) % MOD

prev = prime_factor(a + 1, b + 1)
s = 0
for i in range(a + 1, b + 1):
    aa = prime_factor(i, b + 1)
    # bb = np - (aa, prev)
    for j in range(b + 1):
        if aa[j] == 1 or prev[j] == 1:
            s += 1
            s %= MOD
    prev = aa
    

# n = (numerator) % MOD



print(s)
