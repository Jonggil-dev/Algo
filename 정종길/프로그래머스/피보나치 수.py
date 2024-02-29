def solution(n):
    i = 0
    j = 1

    for _ in range(n - 1):
        k = i + j
        i = j
        j = k
        
    answer = k % 1234567
    return answer