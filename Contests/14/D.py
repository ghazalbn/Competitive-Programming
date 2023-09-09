def is_super_permutation(p, n):
    b = [0] * n
    for i in range(n):
        b[i] = (sum(p[:i+1]) % n) + 1
    return set(b) == set(range(1, n+1))


def generate_permutations(n):
    if n == 1:
        return [[1]]
    else:
        perms = []
        for perm in generate_permutations(n-1):
            for i in range(n):
                perms.append(perm[:i] + [n] + perm[i:])
        return perms


t = int(input())
for i in range(t):
    n = int(input())
    found = False
    for perm in generate_permutations(n):
        if is_super_permutation(perm, n):
            print(*perm)
            found = True
            break
    if not found:
        print(-1)
