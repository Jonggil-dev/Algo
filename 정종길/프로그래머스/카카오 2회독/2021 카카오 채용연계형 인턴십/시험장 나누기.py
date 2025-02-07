'''
1. binary search -> 그룹의 인원이 목표 값 보다 크다면 -> 간선 짜르기 및 감독과 투입
 - 간선을 짜르는 방법은 dfs로 최대 깊이로 들어간 다음 반환되는 결과를 올리면서 판단
 - 현재 노드 + 왼쪽 서브 총합 > 목표 값 : 왼쪽 자녀 짜르기
 - 현재 노드 + 오른쪽 서브 총합 > 목표 값 : 오른쪽 자녀 짜르기
 - 현재 노드 + 왼쪽 서브 + 오른쪽 서브 > 목표 값 : 왼쪽, 오른쪽 중 큰 값 짜르기
2. 감독관이 k 보다 많으면(작으면) -> 목표 값을 늘리기(줄이기)
'''
import sys
sys.setrecursionlimit(100000)

def solution(k, num, links):
    global graph
    n = len(num)
    graph = []

    
    for idx, link in enumerate(links):
        graph.append(link)
        
    r = find_root(n, links)
    start, end = max(num), sum(num)
    
    while start < end:
        mid = (start + end) // 2
        group, _ = dfs(r, mid, num)

        if group + 1 > k:
            start = mid + 1
        else:
            end = mid
    return start

def find_root(n, links):
    sons = [False] * (n + 1)
    for l, r in links:
        sons[l] = sons[r] = True
    for idx, v in enumerate(sons):
        if not v:
            return idx
        
def dfs(node, target, num):
    global graph
    
    if node == -1:
        return (0, 0)
    
    lgc, lpc = dfs(graph[node][0], target, num)
    rgc, rpc = dfs(graph[node][1], target, num)
    total_sum, left_sum, right_sum = lpc + rpc + num[node], lpc + num[node], rpc + num[node]
    
    if total_sum <= target:
        return (lgc + rgc, total_sum)
    
    if min(left_sum, right_sum) <= target:
        return (lgc + rgc + 1, min(left_sum, right_sum))
    

    return (lgc + rgc + 2, num[node])
        
        
        