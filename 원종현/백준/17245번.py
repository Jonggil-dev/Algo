import sys
input=sys.stdin.readline

N=int(input())
li=[]
for i in range(N):
    li+=list(map(int,input().split()))
tot=sum(li)
print(li)
res=0
st,end=0,max(li)
while st<=end:
    mid=(st+end)//2
    tmp=0
    for i in li:
        tmp+=i if i<mid else mid
    if tmp<tot/2:
        st=mid+1
    else:
        res=mid
        end=mid-1
print(res)