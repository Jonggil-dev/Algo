from collections import deque

def solution(maps):
    def BFS(point):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        R, C = len(maps), len(maps[0])
        visited = [[False] * C for _ in range(R)]
        queue = deque([point])
        visited[point[0]][point[1]] = True

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if (0 <= nx < R) and (0 <= ny < C) and maps[nx][ny] != 'X':
                    if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + 1:
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1

        return visited

    for i in range(len(maps)):
        if 'S' in maps[i]:
            start = [i, maps[i].find('S')]
        if 'E' in maps[i]:
            end = [i, maps[i].find('E')]
        if 'L' in maps[i]:
            lever = [i, maps[i].find('L')]

    start_lever = BFS(start)
    if start_lever[lever[0]][lever[1]] == False:
        return -1
    else:
        lever_end = BFS(lever)
        if lever_end[end[0]][end[1]] == False:
            return -1
        else:
            return start_lever[lever[0]][lever[1]] -1 + lever_end[end[0]][end[1]] - 1


maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
maps = ["SOOOOL","XXXOXO","OOOOOO","OXXOXX","OOOOEO"]
print(solution(maps))

