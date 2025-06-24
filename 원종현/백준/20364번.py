import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
li=[int(input()) for _ in range(Q)]
visit=[0]*(N+1)

for i in li:
    now=i
    tmp=[]
    while now!=1:
        if visit[now]:
            tmp.append(now)
        now//=2

    if tmp:
        print(tmp[-1])
    else:
        visit[i]=1
        print(0)
