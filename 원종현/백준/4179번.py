from collections import deque
d=[0,0,1,-1]
R,C=map(int,input().split())
fire=[[0]*C for _ in range(R)]
li=[input() for _ in range(R)]
visit=[[10**4]*C for _ in range(R)]
st=[]
q=deque()
for i in range(R):
    for j in range(C):
        if li[i][j]=='F':
            fire[i][j]=1
            q.append((i,j,1))
        elif li[i][j]=='#':
            fire[i][j]=-1
        elif li[i][j]=='J':
            st=[i,j]

while q:
    x,y,t=q.popleft()
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<R and 0<=ny<C and fire[nx][ny]==0:
            fire[nx][ny]=t+1
            q.append((nx,ny,t+1))

for i in fire:
    print(i)

q=deque()
q.append((st[0],st[1],0))
while q:
    x,y,t=q.popleft()
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<R and 0<=ny<C:
            if t+1<visit[nx][ny] and fire[nx][ny]!=-1 and (fire[nx][ny]==0 or fire[nx][ny]-1>t+1):
                visit[nx][ny]=t+1
                q.append((nx,ny,t+1))
        else:
            print(nx,ny,t+1)
            exit()
print('IMPOSSIBLE')
print('---')
for i in visit:
    print(i)