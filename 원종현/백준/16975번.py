import sys,bisect
input=sys.stdin.readline

def build(le,ri,node):
    if le==ri:
        tree[node]+=li[le]
        return
    mid=(le+ri)//2
    build(le,mid,node*2)
    build(mid+1,ri,node*2+1)
    tree[node]=tree[node*2]+tree[node*2+1]

def ans(le,ri,node,x):
    propagate(node,le,ri)
    if le==ri:
        return tree[node]
    mid=(le+ri)//2
    if x<=mid:
        return ans(le,mid,node*2,x)
    else:
        return ans(mid+1,ri,node*2+1,x)


def query(st,end,node,le,ri,k):
    propagate(node,le,ri)
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        tree[node]+=(ri-le+1)*k
        if le!=ri:
            lazy[node*2]+=k
            lazy[node*2+1]+=k
        return
    mid=(le+ri)//2
    query(st,end,node*2,le,mid,k)
    query(st,end,node*2+1,mid+1,ri,k)
    tree[node]=tree[node*2]+tree[node*2+1]

def propagate(node,le,ri):
    if lazy[node]==0:
        return
    tree[node]+=(ri-le+1)*lazy[node]
    if le!=ri:
        lazy[node*2]+=lazy[node]
        lazy[node*2+1]+=lazy[node]
    lazy[node]=0
def test():
    print('@@')
    for i in range(N):
        print(ans(0,N-1,1,i),end=" ")
    print()
    print('@@')
N=int(input())
li=list(map(int,input().split()))
tree=[0]*(N*4)
lazy=[0]*(N*4)
M=int(input())
build(0,N-1,1)
ans_li=[]
for _ in range(M):
    tmp=list(map(int,input().split()))
    #test()
    if len(tmp)==4:
        _,i,j,k=tmp
        query(i-1,j-1,1,0,N-1,k)
        print(tree)
        print(lazy)
        print('---')
    else:
        _,x=tmp
        ans_li.append(x)
        print(ans(0,N-1,1,x-1))
propagate(1,0,N-1)
print(tree)
print(lazy)

