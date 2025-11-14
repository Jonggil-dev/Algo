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

N,M=map(int,input().split())
tmp_li=[]
c=[[0]*M for _ in range(N)]
for i in range(N):
    tmp=input().rstrip()
    for j in range(M):
        if tmp[j]=='*':
            c[i][j]=1
    tmp_li.append(tmp+'.')

tmp_li.append('.'*(M+1))

length=[[[] for _ in range(M)] for _ in range(N)]
n_max,m_max=0,0
for i in range(N):
    tmp=[]
    f=0
    for j in range(M+1):
        if tmp_li[i][j]=='.':
            if tmp:
                for x,y in tmp:
                    length[x][y].append(n_max)
                n_max+=1
            tmp=[]
        else:
            tmp.append((i,j))

for j in range(M):
    tmp=[]
    for i in range(N+1):
        if tmp_li[i][j]=='.':
            if tmp:
                for x,y in tmp:
                    length[x][y].append(m_max)
                m_max+=1
            tmp=[]
        else:
            tmp.append((i,j))

li=[[] for _ in range(n_max)]
for i in range(N):
    for j in range(M):
        if length[i][j]:
            li[length[i][j][0]].append(length[i][j][1])
check=[-1]*(m_max)
for i in range(n_max):
    visit=[0]*n_max
    func(i)
print(sum([1 for i in check if i!=-1]))