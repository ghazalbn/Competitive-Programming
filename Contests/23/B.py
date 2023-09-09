t = int(input())

for _ in range(t):
    board = [input() for _ in range(3)]
    crossWon = noughtWon = plusWon = False

    # Check rows
    for i in range(3):
        if board[i] == "XXX":
            crossWon = True
        elif board[i] == "OOO":
            noughtWon = True
        elif board[i] == "+++":
            plusWon = True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            crossWon = True
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            noughtWon = True
        elif board[0][i] == board[1][i] == board[2][i] == "+":
            plusWon = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        crossWon = True
    elif board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        noughtWon = True
    elif board[0][0] == board[1][1] == board[2][2] == "+" or board[0][2] == board[1][1] == board[2][0] == "+":
        plusWon = True

    if crossWon:
        print("X")
    elif noughtWon:
        print("O")
    elif plusWon:
        print("+")
    else:
        print("DRAW")
