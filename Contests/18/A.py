t = int(input())
for _ in range(t):
    s = input()
    frequency = {}
    for i in range(len(s)):
        if s[i] in frequency:
            frequency[s[i]] += 1
        else:
            frequency[s[i]] = 1
    even_count = 0
    odd_value = 0
    for key, value in frequency.items():
        even_count += 1 - (value % 2)
        if value % 2:
            odd_value = value
    if even_count > 1 or (odd_value > 1 and even_count):
        print("YES")
    else:
        print("NO")
