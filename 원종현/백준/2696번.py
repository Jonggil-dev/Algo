import sys
import heapq
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    li=[]
    for i in range((N-1)//10+1):
        li+=list(map(int,input().split()))
    lq=[]
    rq=[]
    r=[]
    for i in range(N):
        if i==0:
            r.append(li[i])
            heapq.heappush(lq,(-li[i],li[i]))
            continue
        if i%2==0:
            if li[i]>=rq[0][1]:
                heapq.heappush(rq,(li[i],li[i]))
                t=heapq.heappop(rq)[1]
                r.append(t)
                heapq.heappush(lq,(-t,t))
            else:
                heapq.heappush(lq,(-li[i],li[i]))
                r.append(lq[0][1])
        else:
            heapq.heappush(lq,(-li[i],li[i]))
            while len(lq)!=len(rq):
                if len(lq)>len(rq):
                    t=heapq.heappop(lq)[1]
                    heapq.heappush(rq,(t,t))
                else:
                    t=heapq.heappop(rq)[1]
                    heapq.heappush(lq,(-t,t))
    print(len(r))
    for i in range(0,len(r),10):
        print(*r[i:i+10])