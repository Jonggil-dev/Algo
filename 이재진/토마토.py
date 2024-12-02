import sys
from collections import deque
def sol(ls, n, m, q):
    dij = [[0,1], [1,0], [0,-1], [-1,0]]
    cnt = 0
    ans = 0
    while True:
        new_q = deque()
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in dij:
                ni, nj = ci+di, cj+dj
                if 0<=ni<m and 0<=nj<n and ls[ni][nj] == 0:
                    cnt += 1
                    new_q.append([ni,nj])
                    ls[ni][nj] = 1
        q = new_q
        if not q:
            break
        ans += 1
    return ans, cnt

n, m = list(map(int, sys.stdin.readline().split()))
ls = []
num = 0
q = deque()
for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(tmp)):
        if tmp[j] == 0:
            num += 1
        elif tmp[j] == 1:
            q.append([i,j])
    ls.append(tmp)
if num == 0:
    print(0)
else:
    ans, cnt = sol(ls, n, m, q)
    if num != cnt:
        print(-1)
    else:
        print(ans)


