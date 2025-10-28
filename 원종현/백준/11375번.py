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
li=[]
check=[-1]*(M+1)
for _ in range(N):
    n,*tmp=map(int,input().split())
    li.append(tmp)
    print(n,li)

for i in range(N):
    visit=[0]*N
    func(i)
print(sum([1 for i in check if i!=-1]))