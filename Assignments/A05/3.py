MOD = 10**9 + 7

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


n = int(input())
a = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]

for i in range(n-1):
    if a[i] > a[i+1]:
        dp[i][i+1] = 1

for sz in range(4, n+1, 2):
    for l in range(n-sz+1):
        r = l + sz - 1
        for i in range(l + 1, r + 1, 2):
            if a[l] > a[i]:
                cnt1 = (i-l+1) // 2
                cnt2 = (r-i) // 2
                total = cnt1 + cnt2

                numerator = denominator = 1
                for k in range(1, cnt1+1):
                    numerator = (numerator * (cnt2 + k)) % MOD
                    denominator = (denominator * k) % MOD
                f = (numerator * inverse(denominator)) % MOD
                
                right_dp = dp[i+1][r] if i != r else 1
                left_dp = dp[l+1][i-1] if i != l+1 else 1
                dp[l][r] = (dp[l][r] + (((left_dp*right_dp)% MOD)*f) % MOD) % MOD    

print(dp[0][n-1])