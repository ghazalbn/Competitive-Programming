A, B = input().split()

A_ind, B_ind = 0, 0
for i in range(len(A)):
    if A[i] in B:
        A_ind = i
        B_ind = B.index(A[i])
        break


for i in range(len(B)):
    if i == B_ind:
        row = A
    else:
        row = ['.'] * len(A)
        row[A_ind] = B[i]

    print(*row, sep='')



