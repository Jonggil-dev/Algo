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

N,M=map(int,input().split())
pan=[]
for _ in range(N):
    tmp=list(map(int,input().split()))+[2]
    pan.append(tmp)
pan.append([2]*(M+1))

n_max,m_max=0,0
tmp=[[[] for _ in range(M)] for _ in range(N)]
for i in range(N):
    p=0
    for j in range(M+1):
        if pan[i][j]==1:
            continue
        elif pan[i][j]==2:
            if p==1:
                n_max+=1
            p=0
        else:
            p=1
            tmp[i][j].append(n_max)

for j in range(M):
    p=0
    for i in range(N+1):
        if pan[i][j]==1:
            continue
        elif pan[i][j]==2:
            if p==1:
                m_max+=1
            p=0
        else:
            p=1
            tmp[i][j].append(m_max)

li=[[] for _ in range(n_max)]
for i in range(N):
    for j in range(M):
        if tmp[i][j]:
            li[tmp[i][j][0]].append(tmp[i][j][1])


check=[-1]*(m_max)
for i in range(n_max):
    visit=[0]*(n_max)
    func(i)
print(sum([1 for i in check if i!=-1]))