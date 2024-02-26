from collections import deque
N,M=map(int,input().split())
d1={'A','B','C','D','E','F'}
d2={'a','b','c','d','e','f'}
d=[0,0,1,-1]
st=[0,0]
end=[]
li=[]
for i in range(N):
    tmp=input()
    for j in range(M):
        if tmp[j]=='0':
            st=[i,j]
        elif tmp[j]=='1':
            end.append((i,j))
    li.append(tmp)
visit=[[{i:10**9 for i in range(1<<7)} for _ in range(M)] for _ in range(N)]
q=deque([])
q.append(st+[0])
visit[st[0]][st[1]][0]=0
while q:
    t=q.popleft()
    now=t[:2]
    k=t[2]
    for i in range(4):
        nx=now[0]+d[i]
        ny=now[1]+d[3-i]
        if 0<=nx<N and 0<=ny<M:
            now_val=visit[now[0]][now[1]][k]+1
            if li[nx][ny]!='#':
                if li[nx][ny] in d1:
                    if k&(1<<(ord(li[nx][ny])-65)) and now_val<visit[nx][ny][k]:
                        visit[nx][ny][k]=now_val
                        q.append((nx,ny,k))
                elif li[nx][ny] in d2:
                    if now_val<visit[nx][ny][k|(1<<(ord(li[nx][ny])-97))]:
                        visit[nx][ny][k|(1<<(ord(li[nx][ny])-97))]=now_val
                        q.append((nx,ny,k|(1<<(ord(li[nx][ny])-97))))
                else:
                    if now_val<visit[nx][ny][k]:
                        visit[nx][ny][k]=now_val
                        q.append((nx,ny,k))
res=10**9
for x,y in end:
    res=min(res,min(visit[x][y].values()))
print(res if res!=10**9 else -1)