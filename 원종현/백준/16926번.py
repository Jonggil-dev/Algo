from collections import deque
d=[(0,1),(1,0),(0,-1),(-1,0)]
N,M,R=map(int,input().split())
oqs=[[] for _ in range(min(N,M)//2)]
qs=[deque() for _ in range(min(N,M)//2)]
li=[list(map(int,input().split())) for _ in range(N)]

for i in range(min(N,M)//2):
    st,now,=(i,i),(i,i)
    oqs[i].append(now)
    qs[i].append(now)
    for j in range(4):
        while True:
            tmp=now
            now=(now[0]+d[j][0],now[1]+d[j][1])
            if st==now or not (i<=now[0]<N-i and i<=now[1]<M-i):
                now=tmp
                break
            oqs[i].append(now)
            qs[i].append(now)

for _ in range(R):
    for i in range(min(N,M)//2):
        qs[i].append(qs[i].popleft())

res=[[0]*(M) for _ in range(N)]

for i in range(min(N,M)//2):
    for j in range(len(oqs[i])):
        x,y=oqs[i][j]
        nx,ny=qs[i][j]
        res[x][y]=li[nx][ny]
for i in res:
    print(*i)