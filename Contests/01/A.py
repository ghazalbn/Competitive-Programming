# import math


# def factors(n):
#     count = 0
#     for i in range(1, int(n / 2)):
#         count += n % i == 0
#     return count

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     # a.sort(key=factors)
#     # no = 0
#     # for i in range(2, len(a) + 1):
#     #     prefix = a[:i]
#     #     gcd = prefix[0]
#     #     for j in range(len(prefix)):
#     #         gcd = math.gcd(gcd, prefix[j])
#     #     if gcd > len(prefix):
#     #         no = 1
#     #         break

#     # print('No' if no else 'Yes')

#     min_gcd = math.inf
#     for i in range(len(a)):
#         for j in range(i+1, len(a)):
#             min_gcd = min(min_gcd, math.gcd(a[i], a[j]))
#     print('No' if min_gcd < 2 else 'Yes')


from collections import Counter

def is_good(arr):
    # Compute the greatest common divisor of all elements in arr.
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    # Check if gcd is no more than the length of arr.
    if g > len(arr):
        return False
    else:
        return True

def is_beautiful(arr):
    # Check if all prefixes of arr are good arrays.
    for i in range(2, len(arr)+1):
        if not is_good(arr[:i]):
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if is_beautiful(arr):
        print("Yes")
    else:
        # Check if there are duplicates of the maximum value.
        freq = Counter(arr)
        max_val = max(arr)
        if freq[max_val] > 1:
            print("Yes")
        else:
            print("No")



