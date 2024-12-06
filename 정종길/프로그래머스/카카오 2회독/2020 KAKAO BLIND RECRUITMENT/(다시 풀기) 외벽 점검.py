'''
1. 연산 횟수 -> 8!(dist 순열) * 8(하나의 순열 안에서 순회) * 15(하나의 순열 안에서 weak 순회) = 500만 -> 완전 탐색 가능
2. 시계 방향 완전 탐색 시 반시계 방향은 어짜피 포함이 됨 : a -> b 까지 반시계 방향은 b -> a 시계 방향으로 생각하는 것과 같음
'''

from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    lw = len(weak)
    
    for i in range(lw):
        weak.append(weak[i] + n)
    
    for per in permutations(dist, len(dist)):
        for s in range(lw):
            cnt = 1
            av = weak[s] + per[cnt - 1]
            for c in range(s, s + lw):
                if weak[c] > av:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    av = weak[c] + per[cnt - 1]
            answer = min(answer, cnt)
            
    return answer if answer <= len(dist) else -1