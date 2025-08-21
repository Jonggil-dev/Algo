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

def build(node,left,right):
    lazy[node]=-1
    if left==right:
        tree[node]=1
        return 1
    mid=(left+right)//2
    tree[node]=build(node*2,left,mid)+build(node*2+1,mid+1,right)
    return tree[node]

def propagate(node,st,end):
    if lazy[node]!=-1:
        if st!=end:
            lazy[node*2]=lazy[node]
            lazy[node*2+1]=lazy[node]
        tree[node]=(end-st+1)*lazy[node]
        lazy[node]=-1

def query(st,end,node,left,right):
    propagate(node,left,right)
    if end<left or right<st:
        return 0
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    left_val=query(st,end,node*2,left,mid)
    right_val=query(st,end,node*2+1,mid+1,right)
    return left_val+right_val

def update(left,right,node,idx_l,idx_r,val):
    propagate(node,left,right)
    if idx_r<left or right<idx_l:
        return 0
    if idx_l<=left and right<=idx_r:
        lazy[node]=val
        propagate(node,left,right)
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx_l,idx_r,val)
    update(mid+1,right,node*2+1,idx_l,idx_r,val)
    tree[node]=tree[node*2]+tree[node*2+1]


N=int(input())
li=[0]+list(map(int,input().split()))
M=int(input())
graph=[[] for _ in range(N+1)]
for i in range(2,N+1):
    graph[li[i]].append(i)

st,end=[0]*(N+1),[0]*(N+1)
cnt=0
dfs(1)
tree=[0]*(N*4)
lazy=[-1]*(N*4)
build(1,1,N)

for _ in range(M):
    a,b=map(int,input().split())
    if a==1:
        if st[b]<end[b]:
            update(1,N,1,st[b]+1,end[b],1)
    elif a==2:
        update(1,N,1,st[b]+1,end[b],0)
    else:
        if st[b]==end[b]:
            print(0)
        else:
            print(query(st[b]+1,end[b],1,1,N))
