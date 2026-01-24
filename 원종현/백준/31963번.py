import math,sys
input=sys.stdin.readline


N=int(input())
li=list(map(int,input().split()))
res=0
tmp=[0]*N
for i in range(1,N):
    now=math.ceil(math.log2(li[i-1]/li[i]))+tmp[i-1]
    if now>0:
        tmp[i]=max(0,now)
        res+=tmp[i]
print(res)