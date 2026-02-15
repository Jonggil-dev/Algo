import sys
input=sys.stdin.readline

N=int(input())
li=[0]*100001
for i in range(N):
    now=int(input())
    li[now]=i+1

res=0
for i in range(1,N):
    if li[i]>li[i+1]:
        res+=1
print(res)