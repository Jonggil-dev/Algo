'''
1. 2회차 답안 보다 효율 개선
-> build 시에는 처음부터 확인하는게 아니라 그냥 해당 구조물만 확인
-> detory 시에는 처음부터 재확인
'''

def solution(n, build_frame):
    answer = set()
    for x, y, a, b in build_frame:
        if b == 1:
            if build_check(x, y, a, b, answer):
                answer.add((x, y, a))
        else:
            destory(x, y, a, b, answer)
            
    return sorted(list(answer))

def build_check(x, y, a, b, answer):
    if a == 0:
        if y == 0 or (x, y - 1, 0) in answer or (x, y, 1) in answer or (x - 1, y, 1) in answer:
            return True
    else:
        if ((x, y - 1, 0) in answer or (x + 1, y -1, 0) in answer) or ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
            return True
        
    return False

def total_check(x, y, a, b, answer):
    for x, y, a in answer:
        if not build_check(x, y, a, b, answer):
            return False
    return True

def destory(x, y, a, b, answer):
    answer.remove((x, y, a))
    if not total_check(x, y, a, b, answer):
        answer.add((x, y, a))
    return answer