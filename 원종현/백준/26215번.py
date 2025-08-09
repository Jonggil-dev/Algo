import heapq
N=int(input())
li=list(map(int,input().split()))
hq=[]
if li[0]>1440:
    print(-1)
    exit()

for i in li:
    heapq.heappush(hq,-i)

res=0
while hq:
    if len(hq)>=2:
        a,b=heapq.heappop(hq),heapq.heappop(hq)
        a+=1
        b+=1
        if a!=0:
            heapq.heappush(hq,a)
        if b!=0:
            heapq.heappush(hq,b)
    else:
        a=heapq.heappop(hq)
        a+=1
        if a!=0:
            heapq.heappush(hq,a)
    res+=1
print(-1 if res>1440 else res)