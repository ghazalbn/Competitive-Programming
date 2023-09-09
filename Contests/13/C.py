import math
t = int(input())

# for _ in range(t):
#     n = int(input())
#     # books = []
#     m1 = math.inf
#     m1_i = -1
#     m2 = math.inf
#     m2_i = -1
#     m3 = math.inf
#     m3_i = -1
    
#     for i in range(n):
#         mi, si = input().split()
#         mi = int(mi)
#         si = int(si[0]) + int(si[1]) 
#         if si == 2 and m3 > mi:
#             m3_i = i
#             m3 = mi
#         if mi < m1:
#             m1_i = i
#         elif mi < m2:
#             m2_i = i

#     if m3_i != -1 and m3 < m1 + m2:
#         print(m3)   
#     elif m1_i != -1 and m2_i != -1 and m1 + m2 != float(inf):
#         print(m1+m2)
#     else:
#         print("-1")


for q in range(t):
    b = int(input())
    min01 = math.inf
    min10 = math.inf
    min11 = math.inf
    for w in range(b):
        s = input().split()
        if s[1] == "11" and int(s[0]) < min11:
            min11 = int(s[0])
        if s[1] == "10" and int(s[0]) < min10:
            min10 = int(s[0])
        if s[1] == "01" and int(s[0]) < min01:
            min01 = int(s[0])
    answer = min(min11, min10 + min01)
    if answer == math.inf:
        print("-1")
    else:
        print(answer)
