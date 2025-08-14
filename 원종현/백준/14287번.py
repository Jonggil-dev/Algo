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
li=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for i in range(2,N+1):
    graph[li[i]].append(i)

st,end=[0]*(N+1),[0]*(N+1)
cnt=0
tree=[0]*(N+2)
dfs(1)

for _ in range(M):
    tmp=list(map(int,input().split()))
    if len(tmp)==3:
        _,i,w=tmp
        update(st[i],w)
    else:
        _,i=tmp
        print(query(end[i])-query(st[i]-1))