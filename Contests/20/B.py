import math

t = int(input())
for _ in range(t):
    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    xC, yC = map(int, input().split())
    max_cells = 0

    # if xB == xC and (xB == xA or (yA > min(yB, yC) and yA < max(yB, yC))):
    #     max_cells = abs(yB - yC) + 2
    # elif yB == yC and (yB == yA or (xA > min(xB, xC) and xA < max(xB, xC))):
    #     max_cells = abs(xB - xC) + 2
    # else:
    #     mid_x = (xB + xC) / 2
    #     mid_y = (yB + yC) / 2
    #     max_cells = math.ceil(abs(xA - mid_x) + abs(yA - mid_y)) + 1

    if (xB < xA and xC < xA) or (xB > xA and xC > xA):
        max_cells += min(abs(xA - xB), abs(xA - xC))

    if (yB < yA and yC < yA) or (yB > yA and yC > yA):
        max_cells += min(abs(yA - yB), abs(yA - yC))

    print(max_cells + 1)
