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

N,K=map(int,input().split())
li=[[] for _ in range(N)]
for i in range(K):
    a,b=map(int,input().split())
    li[a-1].append(b-1)

check=[-1]*(N)
for i in range(N):
    visit=[0]*N
    func(i)
print(sum([1 for i in check if i!=-1]))