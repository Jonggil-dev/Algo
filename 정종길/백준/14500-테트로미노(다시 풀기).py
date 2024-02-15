def dfs(i, j, total, cnt=0):
    global res
    if res >= (total + (max_val * (3-cnt))):
        return

    if cnt == 3:
        res = max(total, res)
        return

    else:
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj]:
                    if cnt == 1:
                        visited[ni][nj] = 1
                        dfs(i, j, total + Arr[ni][nj], cnt+1)
                        visited[ni][nj] = 0

                    visited[ni][nj] = 1
                    dfs(ni, nj, total + Arr[ni][nj], cnt+1)
                    visited[ni][nj] = 0

n, m = map(int, input().split())
Arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
max_val = max(map(max, Arr))
res = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, Arr[i][j],0)
        visited[i][j] = 0
print(res)