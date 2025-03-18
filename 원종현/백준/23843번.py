import sys,heapq
input=sys.stdin.readline
N,M=map(int,input().split())
li=sorted(list(map(int,input().split())),reverse=True)
res=[]
for i in li:
    if len(res)<M:
        heapq.heappush(res,i)
    else:
        heapq.heappush(res,i+heapq.heappop(res))
print(max(res))