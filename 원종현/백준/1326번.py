from collections import deque
N=int(input())
li=[0]+list(map(int,input().split()))
a,b=map(int,input().split())

def func(st,end):
    q=deque([])
    q.append(st)
    visit=[-1]*(N+1)
    visit[st]=0
    while q:
        now=q.popleft()
        for i in range(now,N+1,li[now]):
            if visit[i]==-1:
                q.append(i)
                visit[i]=visit[now]+1
                if i==end:
                    return visit[i]
        for i in range(now,0,-li[now]):
            if visit[i]==-1:
                q.append(i)
                visit[i]=visit[now]+1
                if i==end:
                    return visit[i]
    return -1
print(func(a,b))