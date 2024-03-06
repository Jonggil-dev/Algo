import sys
input=sys.stdin.readline
N=int(input())
tree=[0]*(1000001*4)
num=[0]*(1000001)
def query(tar,diff,idx,st,end):
    if end<tar or tar<st:
        return
    tree[idx]+=diff
    mid=(st+end)//2
    if st!=end:
        query(tar,diff,idx*2,st,mid)
        query(tar,diff,idx*2+1,mid+1,end)

def func(count,idx,st,end):
    if st==end:
        return st
    mid=(st+end)//2
    if tree[idx*2]>=count:
        return func(count,idx*2,st,mid)
    else:
        return func(count-tree[idx*2],idx*2+1,mid+1,end)
for i in range(N):
    a,*l=map(int,input().split())
    if a==1:
        res=func(l[0],1,1,1000001)
        print(res)
        query(res,-1,1,1,1000001)
        num[res]-=1
    else:
        query(l[0],l[1],1,1,1000001)
        num[l[0]]+=l[1]