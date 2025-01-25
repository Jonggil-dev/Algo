def solution(A, B):
    A.sort()
    B.sort()

    i = 0
    j = len(B) - 1

    answer = 0

    while i < len(A):
        answer += (A[i] * B[j])
        i += 1
        j -= 1

    return answer