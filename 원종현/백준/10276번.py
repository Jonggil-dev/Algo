import sys,math
input=sys.stdin.readline

def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

R=int(input())
for _ in range(R):
    N,M,K=map(int,input().split())
    room=[[0]*M for _ in range(N)]
    for i in range(K):
        x,y=map(lambda x:math.floor(float(x)),input().split())
        print(x,y)
        room[x][y]+=1
    li=[[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if room[i][j]:
                li[i].append(j)
    check=[-1]*M
    for i in range(N):
        visit=[0]*N
        func(i)
    print(check)
    print(li)
    for i in room:
        print(i)
    print(sum(1 for i in check if i!=-1))