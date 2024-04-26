import heapq
N=int(input())
q=[]
for _ in range(N):
    tmp=list(map(int,input().split()))
    if not q:
        for i in tmp:
            heapq.heappush(q,i)
    else:
        for i in tmp:
            if q[0]<i:
                heapq.heappush(q,i)
                heapq.heappop(q)
print(q[0])