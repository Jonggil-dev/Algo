import heapq
N=int(input())
pre=[]
for i in range(N):
    li=list(map(int,input().split()))
    if len(li)==1 and li[0]==0:
        print(-heapq.heappop(pre) if pre else -1)
    else:
        for j in li[1:]:
            heapq.heappush(pre,-j)
