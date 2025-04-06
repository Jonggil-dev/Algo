'''
1. dfs + 파라메트릭 서치(이분 탐색)
 (1) 파라메트릭 서치로 결과 값 res을 찾아가기
 (2) dfs로 먼저 리프노드까지 내려 간다음 올라오면서 res 보다 커지는지를 파악하고 그룹으로 짜르기

2. dfs 1번당 노드 전체 방문 10,000 조회, 파라메트릭 서치 log100,000,000
-> 이분 탐색 1회당 dfs 1번 발생 -> 10,000 * log100,000,000
-> 20~30만 정도

3. 그룹을 결정 짓는 방법
  (1) 부모 노드 + 자녀에서 올리는 값 <= res -> 그룹에 포함하기
  (2) 부모 노드 + 자녀에서 올리는 값 > res
      1) 부모 + 자녀 값 중 작은 값 1개 <= res -> 작은 자녀만 그룹으로 포함
      2) 1)이 안되면 모두 그룹으로 쪼개기
'''
import sys
sys.setrecursionlimit(1000000)

def solution(k, num, links):
    root = find_root(len(num), links)
    s, e = max(num), 1e9
    answer = 0
    
    while s < e:
        mid = (s + e) // 2
        group, _ = divide(k, num, links, root, mid)
        
        # 만약 group가 k보다 같거나 작다면 -> 그룹의 인원을 줄여야됨 -> e = mid
        if group + 1 <= k:
            e = mid
        
        # 만약 group가 k보다 크다면 -> 그룹의 인원을 늘려야됨 -> s = mid + 1  
        else:
            s = mid + 1

    return s


def find_root(n, links):
    sons = { i for i in range(n) }
    
    for a, b in links:
        if a in sons:
            sons.remove(a)
        if b in sons:
            sons.remove(b)

    for remain in sons:
        return remain

    
def divide(k, num, links, here, mid):
    if here == -1:
        return (0, 0)
    
    group = 0
    
    ls, rs = links[here]
    (g1, p1) = divide(k, num, links, ls, mid)
    (g2, p2) = divide(k, num, links, rs, mid)
    
    group += g1 + g2
    
    if num[here] + p1 + p2 <= mid:
        people = p1 + p2 + num[here]
        
    else:
        if num[here] + min(p1, p2) <= mid:
            people = num[here] + min(p1, p2)
            group += 1

        else:
            people = num[here]
            group += 2

    return (group, people)