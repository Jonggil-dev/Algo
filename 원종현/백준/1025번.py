N,M=map(int,input().split())
li=[input() for _ in range(N)]
res=-1
def check(tmp):
    return int(int(tmp)**0.5)**2==int(tmp)
for x in range(N):
    for y in range(M):
        for r in range(-N,N):
            for c in range(-M,M):
                tmp=''
                nx,ny=x,y
                if r==0 and c==0:
                    continue
                while 0<=nx<N and 0<=ny<M:
                    tmp+=li[nx][ny]
                    if check(tmp):
                        res=max(res,int(tmp))
                    nx+=r
                    ny+=c
print(res)