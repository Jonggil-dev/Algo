import sys
import heapq
input=sys.stdin.readline
d={}
Q=int(input())
res=0
for _ in range(Q):
    tmp=input().rstrip().split()
    if tmp[0]=='1':
        name,K,*li=tmp[1:]
        K=int(K)
        li=[-int(i) for i in li]
        if name in d:
            for i in li:
                heapq.heappush(d[name],i)
        else:
            heapq.heapify(li)
            d[name]=li
    else:
        name,b=tmp[1:]
        b=int(b)
        if name in d:
            while d[name] and b:
                v=-heapq.heappop(d[name])
                res+=v
                b-=1

print(res)