import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

class fan:
    def __init__(self,N):
        self.tree=[0]*(N+2)
        self.N=N

    def query(self,idx):
        s=0
        while idx>0:
            s+=self.tree[idx]
            idx-=idx&-idx
        return s
    def update(self,idx,val):
        while idx<=N+1:
            self.tree[idx]+=val
            idx+=idx&-idx

def dfs(x):
    global cnt
    cnt+=1
    st[x]=cnt
    for i in graph[x]:
        dfs(i)
    end[x]=cnt





N,M=map(int,input().split())
li=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for i in range(2,N+1):
    graph[li[i]].append(i)

st,end=[0]*(N+1),[0]*(N+1)
cnt=0
up_tree=fan(N)
down_tree=fan(N)
dfs(1)
f=1
for _ in range(M):
    tmp=list(map(int,input().split()))
    if len(tmp)==3:
        _,i,w=tmp
        if f:
            up_tree.update(st[i],w)
            up_tree.update(end[i]+1,-w)
        else:
            down_tree.update(st[i],w)
    elif len(tmp)==2:
        _,i=tmp
        print(down_tree.query(end[i])-down_tree.query(st[i]-1)+up_tree.query(st[i]))
    else:
        f=1-f