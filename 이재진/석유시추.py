from collections import deque
def find(land, n, m, i, j):
    dij = [[0,1], [1,0], [0,-1], [-1,0]]
    ans = []
    q = deque()
    q.append([i,j])
    land[i][j] = 0
    
    while q:
        cur = q.popleft()
        ans.append(cur)
        ci, cj = cur[0], cur[1]
        for di, dj in dij:
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and land[ni][nj] == 1:
                q.append([ni,nj])
                land[ni][nj] = 0
    return ans
    
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    ls = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                ans = find(land,n,m,i,j)
                v = [False]*m
                for a in ans:
                    if not v[a[1]]:
                        v[a[1]] = True
                        ls[a[1]] += len(ans)
    answer = max(ls)
    return answer
