import sys
input=sys.stdin.readline

def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

N,M,K=map(int,input().split())
li=[[] for _ in range(N)]
for _ in range(K):
    x,y=map(int,input().split())
    x-=1
    y-=1
    li[x].append(y)

print(li)
check=[-1]*(M+1)
for i in range(N):
    visit=[0]*(N)
    func(i)
print(check)
print(N+M-sum([1 for i in check if i!=-1]))