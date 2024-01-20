import sys,heapq
input=sys.stdin.readline

N=int(input())
tmp=[]
for i in range(N):
    h,a=sorted(map(int,input().split()))
    tmp.append((h,a))
d=int(input())
li=[]
for i in range(N):
    if tmp[i][1]-tmp[i][0]<=d:
        li.append(tmp[i])
li.sort(key=lambda x:x[1])
res=0
q=[]
for r in li:
    if not q:
        heapq.heappush(q,r)
    else:
        while q[0][0]<r[1]-d:
            heapq.heappop(q)
            if not q:
                break
        heapq.heappush(q,r)
    res=max(res,len(q))

print(res)