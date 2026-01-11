from collections import deque


for _ in range(int(input())):
    S,T=map(int,input().split())
    visit=[-1]*200
    q=deque()
    q.append((S,T,0))
    while q:
        s,t,c=q.popleft()
        if s<=t and visit[c]==-1:
            q.append((s*2,t+3,c+1))
            q.append((s+1,t,c+1))
            if s==t:
                print(c)
                break