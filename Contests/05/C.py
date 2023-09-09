from bisect import bisect_left

def max_score_subseq(seq):
    # Compute factorials
    factorials = [1]
    for i in range(1, len(seq) + 1):
        factorials.append(factorials[-1] * i)

    # Find maximum score
    max_score = 1
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            subseq = seq[i:j+1]
            score = 1
            for num in subseq:
                score *= num
            score *= factorials[len(subseq)]
            max_score = max(max_score, score)

    # Find maximum length subsequence with maximum score
    left = 0
    right = 0
    prod = seq[0]
    max_len = 1
    while right < len(seq):
        if prod % seq[right] == 0:
            right += 1
        else:
            prod //= seq[left]
            left += 1
        if prod == max_score:
            max_len = max(max_len, right - left + 1)

    return max_len

# Main code
t = int(input())
for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    for i in range(n):
        print(max_score_subseq(seq[:i+1]), end=" ")
    print()
