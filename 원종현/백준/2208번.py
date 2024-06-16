import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[0]*N
val=0
tmp=[0]
for i in range(N):
    li[i]=int(input())
    val+=li[i]
    tmp.append(val)
res,t=0,0
for i in range(M-1,N):
    t=min(t,tmp[i-(M-1)])
    res=max(res,tmp[i+1]-t)
print(res)