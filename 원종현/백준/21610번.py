import sys
input=sys.stdin.readline
dir=[(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
dia=[(1,1),(1,-1),(-1,1),(-1,-1)]
N,M=map(int,input().split())

li=[[0]*(N+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]

def conv(x,y,dx,dy):
    x-=1
    y-=1
    x=(x+dx)%N
    y=(y+dy)%N
    return [x+1,y+1]

def move(d,s):
    ds=[dir[d][0]*s,dir[d][1]*s]
    for i in range(len(cloud)):
        cloud[i]=conv(cloud[i][0],cloud[i][1],ds[0],ds[1])

def bug(x,y):
    cnt=0
    for dx,dy in dia:
        nx,ny=x+dx,y+dy
        if 1<=nx<=N and 1<=ny<=N and li[nx][ny]:
            cnt+=1
    return cnt

def make_cloud():
    for x in range(1,N+1):
        for y in range(1,N+1):
            if li[x][y]>=2 and (x,y) not in check:
                cloud.append([x,y])
                li[x][y]-=2

cloud=[[N,1],[N,2],[N-1,1],[N-1,2]]
check=set()
for _ in range(M):
    d,s=map(int,input().split())
    move(d,s)
    tmp=[]
    for x,y in cloud:
        li[x][y]+=1
        check.add((x,y))
    for x,y in cloud:
        li[x][y]+=bug(x,y)
    cloud=[]
    make_cloud()
    check=set()
print(sum([sum(i) for i in li]))