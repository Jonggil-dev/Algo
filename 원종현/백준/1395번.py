import sys
input=sys.stdin.readline

def propagate(node,le,ri):
    if lazy[node]%2==1:
        tree[node]=(ri-le+1)-tree[node]
        if le!=ri:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
    lazy[node]=0

def query(st,end,node,le,ri):
    propagate(node,le,ri)
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        return tree[node]
    mid=(le+ri)//2
    return query(st,end,node*2,le,mid)+query(st,end,node*2+1,mid+1,ri)

def update(st,end,node,le,ri):
    propagate(node,le,ri)
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        tree[node]=(ri-le+1)-tree[node]
        if le!=ri:
            lazy[node*2]+=1
            lazy[node*2+1]+=1
        return
    mid=(le+ri)//2
    update(st,end,node*2,le,mid)
    update(st,end,node*2+1,mid+1,ri)
    tree[node]=tree[node*2]+tree[node*2+1]

N,M=map(int,input().split())
tree=[0]*(N*4)
lazy=[0]*(N*4)


for _ in range(M):
    o,s,t=map(int,input().split())
    if o==0:
        update(s,t,1,1,N)
    else:
        print(query(s,t,1,1,N))