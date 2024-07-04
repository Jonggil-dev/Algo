import sys
from collections import defaultdict
input=sys.stdin.readline

N,M,H=map(int,input().split())
dp=[0 for _ in range(H+1)]
for i in range(N):
    li=list(map(int,input().split()))
    tmp=defaultdict(int)
    for j in li:
        for k in range(H-j+1):
            tmp[j+k]+=dp[k]
    for j in li:
        tmp[j]+=1
    for k,v in tmp.items():
        dp[k]+=v
print(dp[H]%10007)