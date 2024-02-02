import sys
sys.setrecursionlimit(10**6)

def checkWater(L):
    for i in range(N):
        for j in range(N):
            if Arr[i][j] <= L:
                visited[i][j] = 1

def dfs(i,j):
    for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ni, nj = i + di, j + dj
        if 0<= ni <N and 0 <= nj <N and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni,nj)


N = int(input())
Arr =[]
maxResult = 0
for _ in range(N):
    tmp = list(map(int,input().split()))
    Arr.append(tmp)
    maxResult = max(max(tmp), maxResult)

res = 0
for k in range(maxResult+1):
    area = 0
    visited = [[0] * N for _ in range(N)]
    checkWater(k)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                area += 1
                visited[i][j] = 1
                dfs(i,j)

    res = max(area, res)


print(res)
