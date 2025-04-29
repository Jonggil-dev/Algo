import sys
input=sys.stdin.readline
MAX=65537
N,K=map(int,input().split())
tree=[0]*(MAX*4)

def build(node,le,ri):
    global tree
    if le==ri:
        tree[node]=1
        return
    mid=(le+ri)//2
    build(2*node,le,mid)
    build(2*node+1,mid+1,ri)
    tree[node]=tree[node*2]+tree[node*2+1]
def update(st,end,idx,tar,val):
    global tree
    if tar<st or tar>end:
        return
    tree[idx]+=val
    if st==end:
        return
    mid=(st+end)//2
    update(st,mid,idx*2,tar,val)
    update(mid+1,end,idx*2+1,tar,val)

def find(st,end,idx,val):
    if st==end:
        return st
    mid=(st+end)//2
    le=tree[idx*2]
    if val<=le:
        return find(st,mid,idx*2,val)
    else:
        return find(mid+1,end,idx*2+1,val-le)

li=[int(input()) for _ in range(N)]
res=0
for i in range(N):
    update(0,MAX,1,li[i],1)
    if i>K-1:
        update(0,MAX,1,li[i-K],-1)
    if i>=K-1:
        res+=find(0,MAX,1,(K+1)//2)
print(res)