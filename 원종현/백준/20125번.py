import sys
input=sys.stdin.readline
N=int(input())
li=[input() for _ in range(N)]
d=[0,0,1,-1]
center=[0,0]
for i in range(N):
    for j in range(N):
        c=0
        for k in range(4):
            nx,ny=i+d[k],j+d[3-k]
            if 0<=nx<N and 0<=ny<N:
                if li[nx][ny]=='*':
                    c+=1
        if c==4:
            center=[i,j]
            break
    if center!=[0,0]:
        break
la,ra,h,lr,rr=-1,-1,-1,0,0
x,y=center
while 0<=x<N and 0<=y<N:
    if li[x][y]=='*':
        la+=1
    y-=1
x,y=center
while 0<=x<N and 0<=y<N:
    if li[x][y]=='*':
        ra+=1
    y+=1
x,y=center
hh=center.copy()
while 0<=x<N and 0<=y<N:
    if li[x][y]=='*':
        h+=1
    else:
        break
    x+=1
    hh[0]+=1
hh[0]-=1
x,y=hh
x+=1
y-=1
while 0<=x<N and 0<=y<N:
    if li[x][y]=='*':
        lr+=1
    else:
        break
    x+=1
x,y=hh
x+=1
y+=1
while 0<=x<N and 0<=y<N:
    if li[x][y]=='*':
        rr+=1
    x+=1
print(*[i+1 for i in center])
print(la,ra,h,lr,rr)