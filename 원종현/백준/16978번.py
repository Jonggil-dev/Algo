import sys
input=sys.stdin.readline

def build(le,ri,node):
    if le==ri:
        tree[node]=li[le]
        return
    mid=(le+ri)//2
    build(le,mid,node*2)
    build(mid+1,ri,node*2+1)
    tree[node]=tree[node*2]+tree[node*2+1]

def update(le,ri,node,idx,val):
    if idx<le or ri<idx:
        return 0
    if le==ri==idx:
        tree[node]=val
        return
    mid=(le+ri)//2
    update(le,mid,node*2,idx,val)
    update(mid+1,ri,node*2+1,idx,val)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(st,end,node,le,ri):
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        return tree[node]
    mid=(le+ri)//2
    return query(st,end,node*2,le,mid)+query(st,end,node*2+1,mid+1,ri)

N=int(input())
li=[0]+list(map(int,input().split()))
tree=[0]*(N*4)
M=int(input())
add_q=[]
k_q=[]
for idx in range(M):
    tmp=list(map(int,input().split()))
    if len(tmp)==3:
        _,i,v=tmp
        add_q.append([i,v])
    else:
        _,k,i,j=tmp
        k_q.append([k,i,j,idx])

k_q.sort(key=lambda x:x[0])
build(0,N,1)

v=0
for now in range(len(k_q)):
    k,i,j,idx=k_q[now]
    if v<k:
        for tar in range(v,k):
            tar_idx,tar_val=add_q[tar]
            update(0,N,1,tar_idx,tar_val)
    tmp_val=query(i,j,1,0,N)
    k_q[now].append(tmp_val)
    v=k
k_q.sort(key=lambda x:x[3])
for i in k_q:
    print(i[4])