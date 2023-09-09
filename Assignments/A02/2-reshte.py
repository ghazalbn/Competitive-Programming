import numpy as np
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ltr, rtl = [1], [1]
    l_count, r_count = {s[0]:1}, {s[n - 1]:1} 
    for i in range(1, n):
        j = n - i - 1

        l_count[s[i]] = l_count.get(s[i], 0) + 1
        r_count[s[j]] = r_count.get(s[j], 0) + 1

        ltr.append(ltr[-1] if (l_count[s[i]] - 1) else ltr[-1] + 1)
        rtl.insert(0, rtl[0] if (r_count[s[j]] - 1) else rtl[0] + 1)

    f_sum = max(np.add(ltr[:-1], rtl[1:]))
    print(f_sum)
