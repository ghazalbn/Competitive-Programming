n = int(input())
summ = int((n * (n + 1)) / 2)
# divisors = [1] * (n + 1)
for i in range(2, n + 1):
    # for j in range(i, n + 1, i):
        # divisors[j] += 1
        # summ += j
    a = n // i
    summ += i * int((a * (a + 1)) / (2))

# summ = sum([i * divisors[i] for i in range(1, n + 1)])

print(summ)