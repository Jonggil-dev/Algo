import sys
input=sys.stdin.readline

N=int(input())

def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

sharks=[]
li=[[] for _ in range(N)]
check=[-1]*N
for i in range(N):
    a,b,c=map(int,input().split())
    sharks.append((i,a,b,c))

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if sharks[i][1]<=sharks[j][1] and sharks[i][2]<=sharks[j][2] and sharks[i][3]<=sharks[j][3]:
            if j not in li[i]:
                li[j].append(i)
for _ in range(2):
    for i in range(N):
        visit=[0]*(N)
        func(i)
res=N-sum([1 for i in check if i!=-1])
print(1 if res==0 else res)
