import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x,dep):
    global cnt
    visit[x]=1
    depth[x]=dep
    cnt+=1
    st[x]=cnt
    for i in graph[x]:
        if not visit[i]:
            dfs(i,dep+1)
    end[x]=cnt

def query(idx):
    s=0
    while idx>0:
        s+=tree[idx]
        idx-=idx&-idx
    return s

def update(idx):
    while idx<=N+1:
        tree[idx]+=1
        idx+=idx&-idx

N,C=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt=0
st,end,depth=[0]*(N+1),[0]*(N+1),[0]*(N+1)
visit=[0]*(N+1)
tree=[0]*(N+2)

dfs(C,1)

Q=int(input())
for _ in range(Q):
    i,A=map(int,input().split())
    if i==1:
        update(st[A])
    else:
        print((query(end[A])-query(st[A]-1))*depth[A])
