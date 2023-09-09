def factorize(n):
    factored = {}
    div = 2
    while div * div <= n:
        while n % div == 0:
            n //= div
            factored[div] = factored.get(div, 0) + 1
        div += 1
    if n > 1:
        factored[n] = factored.get(n, 0) + 1
    return factored

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    factored = {}
    for i in range(n):
        factors = factorize(a[i])
        for factor, power in factors.items():
            factored[factor] = factored.get(factor, 0) + power

    single_count = 0
    result = 0

    for f, pwr in factored.items():
        single_count += pwr % 2
        result += pwr // 2

    result += single_count // 3
    print(result)
