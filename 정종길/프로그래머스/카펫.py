def solution(brown, yellow):
    total = brown + yellow
    answer =[]
    for i in range(1, yellow + 1):
        row = i + 2
        if total % row == 0:
            col = total // row
            if row >= col:
                if (col - 2) * (row - 2) == yellow:
                    answer = [row,col]
    return answer