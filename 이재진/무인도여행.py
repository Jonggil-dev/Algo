from collections import deque
def solution(maps):
    answer = []
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]

    def bfs(i,j):
        dij = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()
        q.append([i,j])
        ans = 0
        while q:
            ci, cj = q.popleft()
            ans += maps[ci][cj]
            for di,dj in dij:
                ni,nj = ci+di, cj+dj
                if maps[ni][nj] != "X" and not visited[ni][nj]:
                    q.append([ni,nj])
                    visited[ni][nj] = 1
        return ans
    
    dij = [[0,1], [1,0], [0,-1], [-1,0]]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "X" and visited[i][j] == -1:
                q = deque()
                q.append([i,j])
                ans = 0
                while q:
                    ci, cj = q.popleft()
                    visited[ci][cj] = 1
                    ans += int(maps[ci][cj])
                    for di,dj in dij:
                        ni,nj = ci+di, cj+dj
                        if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] != "X" and visited[ni][nj] == -1:
                            q.append([ni,nj])
                            visited[ni][nj] = 1
                answer.append(ans)
        answer.sort()
        if not answer:
            answer.append(-1)
    return answer
