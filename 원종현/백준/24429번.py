import sys
input=sys.stdin.readline

def func(st,end):
    global before
    for x in range(st[0],end[0]+1):
        for y in range(st[1],end[1]+1):
            if x==st[0]:
                if y==st[1]:
                    continue
                dp[x][y]=li[x][y]+dp[x][y-1]
            else:
                dp[x][y]=max(dp[x-1][y],dp[x][y-1])+li[x][y]
    before=end
N=int(input())
li=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    li.append(tmp)
P=int(input())
via=[list(map(lambda x:int(x)-1,input().split())) for _ in range(P)]+[[N-1,N-1]]
via.sort(key=lambda x:(x[0],x[1]))
check=(0,0)
for a,b in via:
    if a>check[0] and b<check[1]:
        print(-1)
        exit()
    check=(a,b)
dp=[[0]*N for _ in range(N)]
dp[0][0]=li[0][0]
before=(0,0)

for a,b in via:
    func(before,(a,b))

print(dp[N-1][N-1])