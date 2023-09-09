def generate_blanket(n, m):
    num_set = set()
    B = [[0 for j in range(m)] for i in range(n)]
    num = 1

    for i in range(n):
        for j in range(m):
            B[i][j] = num
            num_set.add(num)
            num += 1

    for i in range(n - 3):
        for j in range(m - 3):
            A = [B[x][j:j+4] for x in range(i,i+4)]
            while A[0][0]^A[0][1]^A[1][0]^A[1][1] != A[2][2]^A[2][3]^A[3][2]^A[3][3] or A[0][2]^A[0][3]^A[1][2]^A[1][3] != A[2][0]^A[2][1]^A[3][0]^A[3][1]:

                A[0][1], A[1][1], A[0][0], A[1][0] = A[1][1], A[0][1], A[1][0], A[0][0]
                A[2][3], A[3][3], A[2][2], A[3][2] = A[3][3], A[2][3], A[3][2], A[2][2]

            for x in range(i,i+4):
                for y in range(j,j+4):
                    B[x][y] = A[x-i][y-j]

    return len(num_set), B



t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    blanket = generate_blanket(n, m)

    print(blanket[0])

    for row in blanket[1]:
        print(' '.join(map(str, row)))
