t = int(input())

# Process each scenario
for _ in range(t):
    R, U, L, D, k = map(int, input().split())

    min_horizontal = min(R, L)
    max_horizontal = max(R, L)
    min_vertical = min(U, D)
    max_vertical = max(U, D)

    if min_horizontal <= min_vertical:
        com_k_horizontal = min(min_horizontal, k)
        min_horizontal -= com_k_horizontal
        k -= com_k_horizontal
        max_vertical += com_k_horizontal

        if k > 0:
            com_k_vertical = min(min_vertical, k)
            min_vertical -= com_k_vertical
            k -= com_k_vertical
            max_horizontal += com_k_vertical

    else:
        com_k_vertical = min(min_vertical, k)
        min_vertical -= com_k_vertical
        k -= com_k_vertical
        max_horizontal += com_k_vertical

        if k > 0:
            com_k_horizontal = min(min_horizontal, k)
            min_horizontal -= com_k_horizontal
            k -= com_k_horizontal
            max_vertical += com_k_horizontal

    if k > 0:
        min_common = min(max_vertical, max_horizontal)
        max_common = max(max_vertical, max_horizontal)

        com_k_common = min(min_common, k)
        max_common += com_k_common
        max_vertical = max_common
        min_common -= com_k_common
        max_horizontal = min_common

    print(int(((max_horizontal - min_horizontal) ** 2) + ((max_vertical - min_vertical) ** 2)))
