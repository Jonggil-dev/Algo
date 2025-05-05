'''
1. 연산 횟수 -> 8!(dist 순열) * 15(하나의 순열 안에서 weak의 출발점 가지 수) * 15(출발한 weak에서 남은 weak까지 순회) -> 900만 -> 완전 탐색
'''
from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    lw = len(weak)
    
    for i in range(lw):
        weak.append(weak[i] + n)
    
    for per in permutations(dist):
        for start_idx in range(lw):
            cnt = 1
            check_limit = weak[start_idx] + per[cnt - 1]
            for weak_idx in range(start_idx + 1, start_idx + lw):
                if weak[weak_idx] > check_limit:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    check_limit = weak[weak_idx] + per[cnt - 1]
            answer = min(answer, cnt)
                
    if answer > len(dist):
        return -1
    
    return answer