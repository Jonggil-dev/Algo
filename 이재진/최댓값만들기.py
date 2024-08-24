def solution(numbers):
    answer = 0
    ls = sorted(numbers)
    answer = ls[-1] * ls[-2]
    return answer
