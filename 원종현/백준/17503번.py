import sys,heapq
input=sys.stdin.readline

N,M,K=map(int,input().split())
li=[]
for i in range(K):
    a,b=map(int,input().split())
    li.append((a,b))
li.sort(key=lambda x:x[1])
tmp=[]
s=0
for i in li:
    if len(tmp)<N:
        heapq.heappush(tmp,i)
        s+=i[0]
        if len(tmp)==N:
            if s>=M:
                print(i[1])
                break
            else:
                s-=heapq.heappop(tmp)[0]
else:
    print(-1)