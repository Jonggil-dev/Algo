'''
1. 브루트포스 : 연산 횟수 990000 -> 대충 러프하게 잡아도 9900(1을 떨구는 최대 횟수) * 100(리프노드 + 높이 탐색)
2. 풀이방법
 
 (1) 우선은 큰 루프는 1을 반복해서 떨구는 것
    -> 큰 루프 안에서 1을 1번 떨굴 때마다 전체 리프 노드에 대해 n <= target[i] <=3n 를 만족하는지 매번 확인 , 이 때 n은 각 리프 노드별 1이 떨어진 횟수
-> n을 전부 1로 떨구면 n, n을 전부 3으로 떨구면 3n 이므로 모든 리프노드에 대해 n <= target[i] <= 3n 동시에 만족해야 답이 될 수 있음 -> 이것이 우선 문제 해결이 가능한 조건
 
 (2) 그리고 모든 리프노드에 대해 n <= target[i] <= 3n에 만족하면, 이제 사전 순으로 가장 빠른 경우를 찾아야됨 
 -> 리프 노드에 떨어지는 순서를 기억
 -> 모든 숫자를 1로 떨어뜨렸다고 생각하고 answer를 생성
 -> 일단 모든 리프노드에 대해 n <= target[i] <= 3n 을 만족하는 순간 break를 했기 때문에, 숫자를 떨구는 전체 횟수에 있어서는 가장 작으며 문제의 조건을 만족하는 경우임 -> 즉 answer의 길이가 가장 짧음을 만족하는 상태
 -> 이제 리프 노드에 떨어진 순서를 뒤에서 부터 조회하며 answer의 1로 떨군거를 3으로 바꿀수 있는지, 바꿀 수 있다면 3으로, 안된다면 2로 그것도 안된다면 1로 바꾸면 끝
'''

def solution(edges, target):
    global graph, drop_info, drop_order
    
    answer = []
    graph = [[] for _ in range(101)]
    point, drop_info, drop_order = {}, {}, []
    
    
    for p, s in edges:
        graph[p].append(s)
    
    for idx, node in enumerate(graph):
        if not node:
            continue
            
        node.sort()
        point[idx] = 0
    
    for idx, t in enumerate(target, start = 1):
        if t:
            drop_info[idx] = 0
        

    while True:
        drop_num(1, point)
        
        if check_valid(target):
            break
            
        if check_end(target):
            return [-1]
    
    answer = [1] * sum(drop_info.values())

    for i in range(len(drop_order) - 1, -1, -1):
        node = drop_order[i]
        if target[node - 1] > drop_info[node]:
            if target[node - 1] == drop_info[node]:
                continue
                
            if target[node - 1] >= drop_info[node] + 2:
                target[node - 1] -= 2
                answer[i] = 3
                continue
            
            else:
                target[node - 1] -= 1
                answer[i] = 2
                continue
                
    return answer

def drop_num(node, point):
    if node not in point:
        drop_info[node] += 1
        drop_order.append(node)
        return
    
    drop_num(graph[node][point[node]], point)
    idx = point[node]
    point[node] = (idx + 1) % len(graph[node])
    
def check_valid(target):
    for k, v in drop_info.items():
        if v > target[k - 1] or 3 * v < target[k - 1]:
            return False
    return True

def check_end(target):
    for k, v in drop_info.items():
        if v < target[k - 1]:
            return False
    return True