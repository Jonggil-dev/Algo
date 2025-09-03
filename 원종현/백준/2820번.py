import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
def dfs(x):
    global cnt
    cnt+=1
    st[x]=cnt
    for i in graph[x]:
        dfs(i)
    end[x]=cnt

def query(idx):
    s=0
    while idx>0:
        s+=tree[idx]
        idx-=idx&-idx
    return s

def update(idx,val):
    while idx<=N+1:
        tree[idx]+=val
        idx+=idx&-idx


N,M=map(int,input().split())
li=[0]*(N+1)
li[1]=int(input())
graph=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    li[i+2]=a
    graph[b].append(i+2)

st,end=[0]*(N+1),[0]*(N+1)
cnt=0
tree=[0]*(N+2)
dfs(1)
for _ in range(M):
    tmp=input().split()
    if len(tmp)==2:
        u,a=tmp
        a=int(a)
        print(query(st[a])+li[a])
    else:
        p,a,x=tmp
        a=int(a)
        x=int(x)
        update(st[a]+1,x)
        update(end[a]+1,-x)