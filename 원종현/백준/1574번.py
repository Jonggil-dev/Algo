import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

R,C,N=map(int,input().split())
if N==0:
    print(max(R,C))
    exit(0)
tmp=[[1]*(C) for _ in range(R)]
for _ in range(N):
    x,y=map(int,input().split())
    x-=1
    y-=1
    tmp[x][y]=0

tmp1=[[0]*C for _ in range(R)]
tmp2=[[0]*C for _ in range(R)]
n_max,m_max=0,0
for i in range(R):
    for j in range(C):
        tmp1[i][j]=n_max
    n_max+=1

for i in range(C):
    for j in range(R):
        tmp2[j][i]=m_max
    m_max+=1
li=[[] for _ in range(n_max)]
for i in range(R):
    for j in range(C):
        if tmp[i][j]:
            li[tmp1[i][j]].append(tmp2[i][j])
check=[-1]*(m_max)
for i in range(n_max):
    visit=[0]*(n_max)
    func(i)
print(sum([1 for i in check if i!=-1]))