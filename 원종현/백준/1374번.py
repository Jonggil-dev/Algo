import sys,heapq
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    a,b,c=map(int,input().split())
    li.append((a,b,c))
li.sort(key=lambda x:(x[1]))
q=[]
r=0
for i in li:
    while q and q[0]<=i[1]:
        heapq.heappop(q)
    heapq.heappush(q,i[2])
    r=max(r,len(q))
print(r)