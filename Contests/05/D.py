MOD = 998244353

def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return primes

n = int(input())
a = list(map(int, input().split()))

primes = sieve_of_eratosthenes(max(a))
freq = [0] * len(primes)
for x in a:
    for i, p in enumerate(primes):
        while x % p == 0:
            freq[i] += 1
            x //= p

if any(x % 2 == 1 for x in a):
    print(0)
else:
    ans = 1
    for f in freq:
        ans = (ans * (f + 1)) % MOD
    print(ans)
