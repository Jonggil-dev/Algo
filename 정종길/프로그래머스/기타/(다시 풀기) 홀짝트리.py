'''
1. 풀이방법 참고 : https://velog.io/@woolzam/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Lv.3-%ED%99%80%EC%A7%9D%ED%8A%B8%EB%A6%AC

2. 하나의 트리에서 노드 % 2 == 연결된 간선 % 2 인 경우가 1개의 노드만 존재한다
 -> 해당 노드를 루트로 하면 홀짝트리가 됨
3. 하나의 트리에서 노드 % 2 != 연결된 간선 % 2 인 경우가 1개의 노드만 존재한다
  -> 해당 노드를 루트로 하면 역홀짝트리가 됨

4. 즉, 임의의 노드 1개에 대해 bfs를 돌리면 해당 트리는 전체 검사가 됨 -> 전체 노드에 대해 bfs를 돌리며 2, 3 조건을 확인 (모든 노드는 1번만 방문하도록 visited로 관리) 
'''

from collections import deque

def solution(nodes, edges):
    answer = [0, 0]
    graph = [[] for _ in range(max(nodes)+1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    visited = set()
    for node in nodes:
        if node not in visited:
            bfs(node, graph, answer, visited)
            
    return answer

def bfs(start, graph, answer, visited):

    odd_even = 0
    reverse_odd_even = 0
    q = deque([start])
    visited.add(start)
    
    while q:
        here = q.popleft()
        if here % 2 == len(graph[here]) % 2:
            odd_even += 1
        else:
            reverse_odd_even += 1
        
        for there in graph[here]:
            if there not in visited:
                q.append(there)
                visited.add(there)

    if odd_even == 1:
        answer[0] += 1
        
    if reverse_odd_even == 1:
        answer[1] += 1
    
    
    
    
    
    
    
    