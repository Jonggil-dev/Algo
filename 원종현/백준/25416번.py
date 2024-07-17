from collections import deque
li=[]
end=[0,0]
for i in range(5):
    tmp=list(map(int,input().split()))
    for j in range(5):
        if tmp[j]==1:
            end=[i,j]
    li.append(tmp)
r,c=map(int,input().split())
d=[0,0,1,-1]
visit=[[0]*5 for _ in range(5)]
q=deque()
q.append((r,c))
visit[r][c]=1

while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<5 and 0<=ny<5 and not visit[nx][ny] and li[nx][ny]!=-1:
            visit[nx][ny]=visit[x][y]+1
            q.append((nx,ny))
print(visit[end[0]][end[1]]-1 if visit[end[0]][end[1]]!=0 else -1)