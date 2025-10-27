import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
MOD=10**9+7
tree=[[0]*11 for _ in range(N*2)]

def update(idx,val,dep):
    idx+=N
    while idx:
        tree[idx][dep]=(tree[idx][dep]+val)%MOD
        idx//=2

def query(le,ri,dep):
    le+=N
    ri+=N
    tmp=0
    while le<=ri:
        if le%2:
            tmp+=tree[le][dep]
            le+=1
        if ri%2==0:
            tmp+=tree[ri][dep]
            ri-=1
        le//=2
        ri//=2
    return tmp

for i in range(N):
    update(li[i]-1,1,0)
    if li[i]==1:
        continue
    for j in range(1,11):
        tmp=query(0,li[i]-2,j-1)
        update(li[i]-1,tmp,j)

print(tree[1][-1]%MOD)