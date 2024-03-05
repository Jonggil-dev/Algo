import heapq
N,D=map(int,input().split())
dp=[0]+list(map(int,input().split()))
hq=[]
for i in range(1,N+1):
    while hq and i-hq[0][1]>D:
        heapq.heappop(hq)
    if hq:
        dp[i]+=-hq[0][0]
    if dp[i]>0:
        heapq.heappush(hq,(-dp[i],i))
print(max(dp[1:]))