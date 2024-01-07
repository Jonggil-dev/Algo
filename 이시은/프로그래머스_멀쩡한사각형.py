# 프로그래머스 멀쩡한 사각형
# 풀이 아이디어 + 시간초과 해결이 관건

import math
def solution(w,h):
    gcd = math.gcd(w, h)
    sub_w = int(w / gcd)
    sub_h = int(h / gcd)

    answer = 0
    if sub_w <= sub_h:
        for i in range(1, sub_w):
            answer += int(sub_h * i / sub_w)
        answer *= 2
        answer += ((w - sub_w) * sub_h)
    else:
        for i in range(1, sub_h):
            answer += int(sub_w * i / sub_h)
        answer *= 2
        answer += ((h - sub_h) * sub_w)
    return answer * gcd

print(solution(8, 12))