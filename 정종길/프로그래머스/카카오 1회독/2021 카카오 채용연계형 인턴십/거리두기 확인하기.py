def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

def check(place):
    r = len(place)
    c = len(place[0])
    
    for i in range(r):
        for j in range(c):
            if place[i][j] == "P":
                for dx, dy in (0, 1), (1, 0), (0, -1):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if place[nx][ny] == "P":
                            return 0
                        
                        if place[nx][ny] == "O":
                            if dx == 0 and dy == -1:
                                nnx, nny = nx + 1, ny + 0
                                if 0 <= nnx < r and 0 <= nny < c:
                                    if place[nnx][nny] == "P":
                                        return 0
                                
                            elif dx == 1 and dy == 0:
                                for ddx, ddy in (0, -1), (1, 0), (0, 1):
                                    nnx, nny = nx + ddx, ny + ddy
                                    if 0 <= nnx < r and 0 <= nny < c:
                                        if place[nnx][nny] == "P":
                                            return 0
                            else:
                                nnx, nny = nx + 1, ny + 0
                                for ddx, ddy in (1, 0), (0, 1):
                                    nnx, nny = nx + ddx, ny + ddy
                                    if 0 <= nnx < r and 0 <= nny < c:
                                        if place[nnx][nny] == "P":
                                            return 0
    return 1
    