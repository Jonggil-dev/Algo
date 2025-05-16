import sys,heapq
input=sys.stdin.readline

N=int(input())
hq=[]
max_day=0
for _ in range(N):
    d,w=map(int,input().split())
    max_day=max(max_day,d)
    heapq.heappush(hq,(-w,d))

day=[0]*(max_day+1)
while hq:
    w,d=heapq.heappop(hq)
    for i in range(d,0,-1):
        if not day[i]:
            day[i]=-w
            break
print(sum(day))