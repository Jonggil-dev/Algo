import sys
input=sys.stdin.readline

def func(x,y,flag):
    global idx,g_flag
    while True:
        if flag:
            if x==N or y==N:
                break
        else:
            if x==N or y<0:
                break
        if hole[x][y]==0:
            if g_flag:
                idx+=1
                g_flag=0
            tmp_li[x][y].append(idx)
        else:
            g_flag=1
        x+=1
        if flag:y+=1
        else:y-=1
    g_flag=1

def get(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or get(check[i]):
            check[i]=x
            return 1
    return 0

N=int(input())
M=int(input())
hole=[[0]*N for _ in range(N)]
for i in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    hole[x][y]=1
tmp_li=[[[] for _ in range(N)] for _ in range(N)]
idx=0
x_max,y_max,g_flag=0,0,0
for x in range(N-1,-1,-1):
    y=0
    func(x,y,1)

for y in range(1,N):
    x=0
    func(x,y,1)
x_max=idx+1
idx,g_flag=0,0
for y in range(N):
    x=0
    func(x,y,0)
for x in range(1,N):
    y=N-1
    func(x,y,0)
y_max=idx+1

li=[[] for _ in range(x_max)]
for i in range(N):
    for j in range(N):
        if tmp_li[i][j]:
            x,y=tmp_li[i][j]
            li[x].append(y)

check=[-1]*y_max
for i in range(x_max):
    visit=[0]*(x_max)
    get(i)
print(sum([1 for i in check if i!=-1]))