import sys
input=sys.stdin.readline
dir=[0,0,1,-1]
N=int(input())
li=[[0]*(N+1) for _ in range(N+1)]
d={}
friendly={}
res=0
def seat(x,y,a):
    li[x][y]=a
    d[a]=(x,y)

def get_side(x,y):
    t=0
    for i in range(4):
        nx,ny=x+dir[i],y+dir[3-i]
        if 1<=nx<=N and 1<=ny<=N and li[nx][ny]==0:
            t+=1
    return t

def get_side_friends(x,y,friends):
    t=0
    for i in friends:
        if i in d:
            nx,ny=d[i]
            if abs(nx-x)+abs(ny-y)==1:
                t+=1
    return t

for _ in range(N**2):
    A,*friends=map(int,input().split())
    friendly[A]=friends
    tmp=[]
    for x in range(1,N+1):
        for y in range(1,N+1):
            if li[x][y]==0:
                now=[get_side_friends(x,y,friends),get_side(x,y),x,y]
                tmp.append(now)
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    seat(tmp[0][2],tmp[0][3],A)

for k,v in d.items():
    x,y=v
    r=get_side_friends(x,y,friendly[k])
    res+=[0,1,10,100,1000][r]
print(res)