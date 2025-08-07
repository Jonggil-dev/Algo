import sys
input=sys.stdin.readline

# [구간최소,구간최대,구간최대상승]

def make(le,ri):
    return [min(tree[le][0],tree[ri][0]),max(tree[le][1],tree[ri][1]),max(tree[le][2],tree[ri][2],tree[ri][1]-tree[le][0])]

def build(node,le,ri):
    if le==ri:
        tree[node]=[li[le],li[ri],0]
        return
    mid=(le+ri)//2
    build(node*2,le,mid)
    build(node*2+1,mid+1,ri)
    tree[node]=make(node*2,node*2+1)

def update(le,ri,node,idx,val):
    if idx<le or ri<idx:
        return
    if le==ri==idx:
        li[idx]=val
        tree[node]=[val,val,0]
        return
    mid=(le+ri)//2
    update(le,mid,node*2,idx,val)
    update(mid+1,ri,node*2+1,idx,val)
    tree[node]=make(node*2,node*2+1)

def query(st,end,le,ri,node):
    if end<le or st>ri:
        return [10**11,-10**11,-10**11]
    if st<=le and ri<=end:
        return tree[node]
    mid=(le+ri)//2
    le_val=query(st,end,le,mid,node*2)
    ri_val=query(st,end,mid+1,ri,node*2+1)
    return [min(le_val[0],ri_val[0]),max(le_val[1],ri_val[1]),max(le_val[2],ri_val[2],0 if abs(ri_val[1]-le_val[0])>=10**10 else ri_val[1]-le_val[0])]

N=int(input())
li=list(map(int,input().split()))
tree=[[] for _ in range(N*4)]
Q=int(input())
build(1,0,N-1)
print(tree)
for _ in range(Q):
    a,b,c=map(int,input().split())
    if a==1:
        print('--')
        print(tree)
        update(0,N-1,1,b-1,c)
        print(tree)
        print('--')
    else:
        tmp=query(b-1,c-1,0,N-1,1)
        print(tmp)
print(tree)