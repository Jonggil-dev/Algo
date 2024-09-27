import sys,heapq
input=sys.stdin.readline

N=int(input())
tmp=''.join(list(map(lambda x:str(int(x)-1), input().split())))
res=''.join(sorted(tmp))
M=int(input())
mo=[]
for i in range(M):
    mo.append(list(map(int,input().split())))

dic={}
dic[tmp]=0
q=[]
heapq.heappush(q,(tmp,0))
while q:
    now,dist=heapq.heappop(q)
    for l,r,c in mo:
        cost=dist+c
        next=now[:l-1]+now[r-1]+now[l:r-1]+now[l-1]+now[r:]
        if next not in dic or dic[next]>cost:
            dic[next]=cost
            heapq.heappush(q,(next,cost))
if res not in dic:
    print(-1)
else:
    print(dic[res])