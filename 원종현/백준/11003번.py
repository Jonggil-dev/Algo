import heapq
N,L=map(int,input().split())
dp=list(map(int,input().split()))
hq=[]
D=[0]*(N)

for i in range(N):
    while hq and (i-hq[0][1]>=L or hq[0][0]>dp[i]):
        heapq.heappop(hq)
    heapq.heappush(hq,(dp[i],i))
    D[i]=hq[0][0]
print(*D)