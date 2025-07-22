import heapq

N,M=map(int,input().split())
li=list(map(int,input().split()))
q=[]
for i in li:
    heapq.heappush(q,-i)
li2=list(map(int,input().split()))
res=0
for i in li2:
    now=-heapq.heappop(q)
    if now-i<0:
        res=1
        break
    heapq.heappush(q,-(now-i))

print([1,0][res])