# 프로그래머스 두 원 사이의 정수 쌍

import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        bottom = math.sqrt(r1**2 - min(r1, x)**2)
        top = math.sqrt(r2**2 - x**2)
        
        answer += math.floor(top) - math.ceil(bottom) + 1
                
    return answer * 4