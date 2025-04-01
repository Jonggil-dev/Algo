'''
1. 처음 풀 때 햇갈렸던 것 (완전 탐색 or 다익스트라)
(1) 다익스트라의 경우
: 어떤 가중치로? 문제를 풀어나가야 될지 모르겠음, 코스트 대비 획득 점수로 설계 해야 될 꺼 같은데, 코딩력과 알고력 2가지 점수로 나누어지니까 설계가 안됨

(2) 완전 탐색의 경우
입력이 0, 0, problems : [[알고: 150, 코딩: 150]] 일 때
0, 0 -> 150, 150 까지 갈 때 최소 행동횟수 300 (1점씩 150점, 150점 올리기)
근데 각 행동 별 알고 +1 or 코딩 +1 선택 할 수 있음 -> 2 ^ (300) 


(3) 완전 탐색 + 메모이제이션
1. 가로를 알고력, 세로를 코딩력 -> 150 * 150 상태를 가짐
2. 각 상태별로 모든 problems 순회해서 풀 수 있는 거 점수 올리기 or 알고력 + 1 or 코딩력 + 1 -> 102가지 순회
-> 151 * 151 * 102 = 2250000

3. 시작 alp, cop가 max 보다 높은 경우 처리하는 게 조금 헷갈림
'''

def solution(alp, cop, problems):
    max_alp, max_cop = max(problems, key = lambda x : x[0])[0], max(problems, key = lambda x : x[1])[1]
    max_alp, max_cop = max(alp, max_alp), max(cop, max_cop)
    memo = [[1e9] * (max_cop + 1) for _ in range(max_alp + 1)]
    memo[alp][cop] = 0
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na, nc = min(a + alp_rwd, max_alp), min(c + cop_rwd, max_cop)
                    memo[na][nc] = min(memo[na][nc], memo[a][c] + cost)
            na, nc = min(a + 1, max_alp), min(c + 1, max_cop)
            memo[na][c] = min(memo[na][c], memo[a][c] + 1)
            memo[a][nc] = min(memo[a][nc], memo[a][c] + 1)
    return memo[-1][-1]