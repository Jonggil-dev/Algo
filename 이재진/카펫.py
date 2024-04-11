def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(1, total):
        if total % i == 0 and i >= (total // i):
            if (i + total//i) * 2 - 4 == brown:
                return [i, total//i]
    return answer
