import sys
input=sys.stdin.readline

def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

N=int(input())
tmp=[]
for _ in range(N):
    tmp.append(input().rstrip()+'X')
tmp.append('X'*(N+1))
graph=[[[] for _ in range(N)] for _ in range(N)]
n_max,m_max=0,0
for i in range(N):
    f=0
    for j in range(N+1):
        if tmp[i][j]=='X':
            if not f:
                continue
            f=0
            n_max+=1
        else:
            f=1
            graph[i][j].append(n_max)
for i in range(N):
    f=0
    for j in range(N+1):
        if tmp[j][i]=='X':
            if not f:
                continue
            f=0
            m_max+=1
        else:
            f=1
            graph[j][i].append(m_max)

li=[[] for _ in range(n_max)]
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            li[graph[i][j][0]].append(graph[i][j][1])
check=[-1]*(m_max)
for i in range(n_max):
    visit=[0]*(n_max)
    func(i)
print(sum([1 for i in check if i!=-1]))