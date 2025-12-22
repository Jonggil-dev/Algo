import sys
input=sys.stdin.readline

def func(x):
    if visit[x]==idx:
        return 0
    visit[x]=idx

    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

for _ in range(int(input())):
    N,M=map(int,input().split())
    max_x=0
    tmp=[]
    for i in range(M):
        t1,t2,a,*q=map(int,input().split())
        tmp.append([t1,t2,*q])
        max_x=max(max_x,t2)
    li=[set() for _ in range(max_x+1)]
    for t1,t2,*q in tmp:
        for i in range(t1,t2):
            li[i]=li[i].union(set(q))
    idx=0
    visit=[0]*(max_x+1)
    check=[-1]*(N+1)
    for i in range(max_x):
        idx+=1
        func(i)
    v=0
    res=0
    for i in check[1:]:
        if i!=-1:
            v+=1
            res=max(res,i)
    if v!=N:
        print(-1)
    else:
        print(res+1)