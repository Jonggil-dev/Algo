import sys
input=sys.stdin.readline
N=int(input())
def func(left,right,node,idx):
    tree[node]+=1
    if left==right:
        return 0
    mid=(left+right)//2
    if idx<=mid:
        return func(left,mid,node*2,idx)+tree[node*2+1]
    else:
        return func(mid+1,right,node*2+1,idx)
tree=[0]*(N*4)
dic={}
li=list(map(int,input().split()))
for i in range(N):
    dic[li[i]]=i+1
res=0
li=list(map(int,input().split()))
for i in range(N):
    res+=func(1,N,1,dic[li[i]])
print(res)