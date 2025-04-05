'''
1. 트랩의 상태 기록 하면서 다익스트라 돌리기
-> 1000log1000(다익스트라) * 2 ^ 10(트랩의 상태 2^10)
-> 연산 횟수 : 10,000,000

2. 트랩의 상태는 트랩 번호를 인덱스로 뽑아내고 비트마스킹으로 관리
3. 트랩의 상태에 따라 건널지 말지 고려
-> 심플하게 나누기
1) here, there 중 트랩이 1개만 켜져 있다 -> 역방향 화살표
2) here, there 중 트랩이 0 or 2개가 켜져 있다 -> 정방향 화살표
'''

import heapq
def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n + 1)]
    trap_idxs = {}
    
    for n1, n2, t in roads:
        graph[n1].append((n2, t, 1))
        graph[n2].append((n1, t, -1))
    
    for idx, num in enumerate(traps, start = 1):
        trap_idxs[num] = idx
    
    traps = set(traps)
    times = [{} for _ in range(n + 1)]
    
    q = [(0, start, 0)]
    times[start][0] = 0
    
    while q:
        time, here, trap_state = heapq.heappop(q)
        if here == end:
            return time
    
        if time > times[here][trap_state]:
            continue
        
        now_valid = 1
        
        
        # 지금 내 위치가 트랩인지
        if here in traps:
            here_idx = trap_idxs[here]
            if not (1 << here_idx) & trap_state:
                now_valid *= -1
            trap_state = trap_state ^ (1 << here_idx)

        
        # 인접 노드가 트랩인지 + 켜져 있는지
        for there, weight, direction in graph[here]:
            there_valid = 1
            if there in traps:
                there_idx = trap_idxs[there]
                if (1 << there_idx) & trap_state:
                    there_valid *= -1
            if (now_valid * there_valid == 1 and direction == 1) or (now_valid * there_valid == -1 and direction == -1):

                
                if trap_state in times[there]:
                    if time + weight <= times[there][trap_state]:
                        times[there][trap_state] = time + weight
                        heapq.heappush(q, (time + weight, there, trap_state))
                else:
                    times[there][trap_state] = time + weight
                    heapq.heappush(q, (time + weight, there, trap_state))
                
        