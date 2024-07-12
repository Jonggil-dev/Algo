def solution(sequence, k):
    answer = []
    n = len(sequence)
    num = 0
    for i in range(n-1, -1, -1):
        num += sequence[i]
        if num > k:
            num -= sequence.pop()
        if num == k:
            while sequence[i-1] == sequence[-1] and i>0:
                i -= 1
                sequence.pop()
            return [i, len(sequence)-1]
