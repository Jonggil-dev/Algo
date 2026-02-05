import sys
input=sys.stdin.readline
N=int(input())
li1,li2=[0]*1000001,[0]*1000001
dp=[0]*1000001
for i in range(N):
    a,b=map(int,input().split())
    li1[a]+=1
    li2[b]+=1

for i in range(1,1000001):
    dp[i]=dp[i-1]+li1[i]-li2[i-1]
Q=int(input())
res=list(map(int,input().split()))
for i in res:
    print(dp[i])