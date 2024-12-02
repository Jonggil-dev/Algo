import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())

li=[int(input()) for _ in range(N)]
tree=[0]*(N*4)
lazy=[0]*(N*4)

def propagate(node,le,ri):
    if lazy[node]:
        tree[node]+=(ri-le+1)*lazy[node]
        if le!=ri:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0
def build(node,le,ri):
    if le==ri:
        tree[node]=li[le]
        return
    mid=(le+ri)//2
    build(node*2,le,mid)
    build(node*2+1,mid+1,ri)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(st,end,node,le,ri):
    propagate(node,le,ri)
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        return tree[node]
    mid=(le+ri)//2
    le_val=query(st,end,node*2,le,mid)
    ri_val=query(st,end,node*2+1,mid+1,ri)
    return le_val+ri_val

def update(st,end,node,le,ri,val):
    propagate(node,le,ri)
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        tree[node]+=(ri-le+1)*val
        if le!=ri:
            lazy[node*2]+=val
            lazy[node*2+1]+=val
        return
    mid=(le+ri)//2
    update(st,end,node*2,le,mid,val)
    update(st,end,node*2+1,mid+1,ri,val)
    tree[node]=tree[node*2]+tree[node*2+1]

build(1,0,N-1)
for i in range(M+K):
    tmp=list(map(int,input().split()))
    if len(tmp)==4:
        a,b,c,d=tmp
        update(b-1,c-1,1,0,N-1,d)
    else:
        a,b,c=tmp
        print(query(b-1,c-1,1,0,N-1))
