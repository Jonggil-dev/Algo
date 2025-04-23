import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
T=int(input())
def check(x,n):
    if x==n and visit[x]:
        return
    visit[x]=1
    check(g[x],n)
for _ in range(T):
    N=int(input())
    li=list(map(int,input().split()))
    g=[0]*(N+1)
    visit=[0]*(N+1)
    for i in range(N):
        g[i+1]=li[i]
    res=0
    for i in li:
        if not visit[i]:
            res+=1
            check(i,i)
    print(res)