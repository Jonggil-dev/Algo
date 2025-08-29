import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

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
st,end=[0]*(N+1),[0]*(N+1)
cnt=0
graph=[[] for _ in range(N+1)]
for i in range(2,N+1):
    graph[li[i]].append(i)
dfs(1)
tree=[0]*(N+2)
print(st,end)

for _ in range(M):
    tmp=list(map(int,input().split()))
    if len(tmp)==3:
        _,i,w=tmp
        update(st[i],w)
        update(end[i]+1,-w)

    else:
        _,i=tmp
        print(query(st[i]))
