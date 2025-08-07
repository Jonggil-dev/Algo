import sys,bisect
input=sys.stdin.readline


def build(le,ri,node):
    if le==ri:
        tree[node].append(li[le])
        return
    mid=(le+ri)//2
    build(le,mid,node*2)
    build(mid+1,ri,node*2+1)
    tree[node]=merge(tree[node*2],tree[node*2+1])

def merge(li1,li2):
    tmp=[]
    le,ri=0,0
    while le<len(li1) and ri<len(li2):
        if li1[le]<li2[ri]:
            tmp.append(li1[le])
            le+=1
        else:
            tmp.append(li2[ri])
            ri+=1
    tmp.extend(li1[le:])
    tmp.extend(li2[ri:])
    return tmp

def query(st,end,node,le,ri,k):
    if end<le or ri<st:
        return 0
    if st<=le and ri<=end:
        return len(tree[node])-bisect.bisect_right(tree[node],k)
    mid=(le+ri)//2
    return query(st,end,node*2,le,mid,k)+query(st,end,node*2+1,mid+1,ri,k)
N=int(input())
li=list(map(int,input().split()))
tree=[[] for _ in range(N*4)]
build(0,N-1,1)
M=int(input())
r=0
print(tree)
for _ in range(M):
    a,b,c=map(int,input().split())
    i,j,k=a^r,b^r,c^r
    print(f'before {r},',end='')
    r=query(i-1,j-1,1,0,N-1,k)
    print(r)
    print(f'after {r} {a},{b},{c} -> {i},{j},{k}')