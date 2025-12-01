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


N,M=map(int,input().split())
li=[[] for _ in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    li[B].append(A)

check=[-1]*(N)
for i in range(N):
    visit=[0]*N
    func(i)
print('YES' if sum([1 for i in check if i!=-1])==N else'NO')