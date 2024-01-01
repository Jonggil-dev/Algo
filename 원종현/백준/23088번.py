import sys,heapq
input=sys.stdin.readline

N=int(input())
q=[]
q2=[]
for i in range(N): # t: 실행요청 시점, p: 초기 우선순위, b: i번 프로세스의 실행시간
    t,p,b=map(int,input().split())
    heapq.heappush(q,(t,p,b,i+1))


c=0
while q or q2:
    while q and q[0][0]<=c:
        t,p,b,i=heapq.heappop(q)
        heapq.heappush(q2,(-p+t,b,i))
    if q2:
        p,b,i=heapq.heappop(q2)
        print(i,end=' ')
        c+=b
    else:
        c+=1