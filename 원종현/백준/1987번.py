import sys
sys.setrecursionlimit(10**8)
d=[0,0,1,-1]
R,C=map(int,input().split())
li=[input() for _ in range(R)]
dic={}
res=0
def dfs(now,cnt,visit):
    global res
    res=max(res,cnt)
    if visit==(1<<26)-1 or res==26:
        return
    for i in range(4):
        nx,ny=now[0]+d[i],now[1]+d[3-i]
        if 0<=nx<R and 0<=ny<C and not visit&(1<<ord(li[nx][ny])-65):
            dfs((nx,ny),cnt+1,visit|(1<<(ord(li[nx][ny])-65)))

dfs((0,0),1,(1<<ord(li[0][0])-65))
print(res)