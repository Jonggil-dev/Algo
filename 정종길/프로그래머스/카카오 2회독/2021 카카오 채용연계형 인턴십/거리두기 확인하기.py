from collections import deque
def solution(places):
    answer = []
    
    for place in places:
        answer.append(check_distance_rule(place))
    return answer

def check_distance_rule(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                q = deque([(i, j, 0)])
                visited = {(i, j)}
                while q:
                    i, j, cnt = q.popleft()
                    if cnt < 2:
                        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < 5 and 0 <= nj < 5 and (ni, nj) not in visited:
                                if place[ni][nj] == "P":
                                    return 0
                                
                                if place[ni][nj] == "O":
                                    q.append((ni, nj, cnt + 1))
                                    visited.add((ni, nj))
    return 1
                