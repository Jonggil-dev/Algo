from collections import deque
def solution(players, m, k):
    answer = 0
    server_info = deque()
    
    for player in players:
        current_capacity = m * (len(server_info) + 1) - 1
        if player > current_capacity:
            more_capcity = ((player - current_capacity - 1) // m) + 1
            for _ in range(more_capcity):
                server_info.append(k)
                answer += 1
        server_update(server_info)
        
    return answer

def server_update(server_info):
    n = len(server_info)
    for _ in range(n):
        v = server_info.popleft()
        if v == 1:
            continue
        else:
            server_info.append(v-1)
        
    return