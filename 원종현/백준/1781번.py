import sys,heapq
input=sys.stdin.readline
N=int(input())
A=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append((a,b))
A.sort(key=lambda x:(x[0],-x[1]))
q=[]
for i in A:
    heapq.heappush(q,i[1])
    if i[0]<len(q):
        heapq.heappop(q)
print(sum(q))