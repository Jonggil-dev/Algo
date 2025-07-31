import sys
input=sys.stdin.readline

N=int(input())
li=[[] for _ in range(N)]
tree=[0]*(N*8)
res=0
def update(le,ri,node,idx):
    if idx<le or ri<idx:
        return 0
    if le==ri==idx:
        tree[node]=1
        return
    mid=(le+ri)//2
    update(le,mid,node*2,idx)
    update(mid+1,ri,node*2+1,idx)
    tree[node]=tree[node*2]+tree[node*2+1]
def query(st,end,node,le,ri):
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        return tree[node]
    mid=(le+ri)//2
    return query(st,end,node*2,le,mid)+query(st,end,node*2+1,mid+1,ri)

for i in range(N*2):
    now=int(input())
    li[now-1].append(i+1)
li.sort(key=lambda x:x[0])
print(li)

for x,y in li:
    res+=query(x,y,1,0,N*2-1)
    update(0,N*2-1,1,y)
print(res)