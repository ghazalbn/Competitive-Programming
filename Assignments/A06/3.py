from math import factorial

n, k = map(int, input().split())

ans = [1]
ans.append(ans[0] + n * (n - 1) // 2)
ans.append(ans[1] + n * (n - 1) * (n - 2) // 3)
ans.append(ans[2] + n * (n - 1) * (n - 2) * (n - 3) * 3 // 8)

print(ans[k - 1])
