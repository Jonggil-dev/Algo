from collections import deque
N,M=map(int,input().split())
d=[0,0,1,-1]
li=[]
coin=[]
for i in range(N):
    tmp=list(input())
    for j in range(M):
        if tmp[j]=='o':
            coin.append((i,j))
    li.append(tmp)

res=11
q=deque()
visit=set()
visit.add((coin[0][0],coin[0][1],coin[1][0],coin[1][1]))
q.append((coin[0][0],coin[0][1],coin[1][0],coin[1][1],0))
flag=0
while q:
    x1,y1,x2,y2,c=q.popleft()
    if c>=10:
        break
    for i in range(4):
        nx1,ny1,nx2,ny2=x1+d[i],y1+d[3-i],x2+d[i],y2+d[3-i]
        if (not (0<=nx1<N) or not(0<=ny1<M)) and (0<=nx2<N and 0<=ny2<M):
            res=min(res,c+1)
            flag=1
            break
        elif (not (0<=nx2<N) or not(0<=ny2<M))  and (0<=nx1<N and 0<=ny1<M):
            res=min(res,c+1)
            flag=1
            break
        elif (0<=nx1<N and 0<=ny1<M) and (0<=nx2<N and 0<=ny2<M):
            dx1,dy1=x1,y1
            if li[nx1][ny1]!='#':
                dx1,dy1=nx1,ny1
            dx2,dy2=x2,y2
            if li[nx2][ny2]!='#':
                dx2,dy2=nx2,ny2
            if (dx1,dy1,dx2,dy2) not in visit:
                q.append((dx1,dy1,dx2,dy2,c+1))
                visit.add((dx1,dy1,dx2,dy2))

    if flag:
        break

print(-1 if res>=11 else res)