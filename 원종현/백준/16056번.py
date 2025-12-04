import sys
input=sys.stdin.readline

def func(x,s):
    if visit[x]:
        return 0
    visit[x]=1

    tmp=li[s] if x>M else li[x]
    for i in tmp:
        if check[i]==-1 or func(check[i],s):
            check[i]=x
            return 1
    return 0

M,N,K=map(int,input().split())
li=[[] for _ in range(M+1)]
for i in range(K):
    x,y=map(int,input().split())
    li[x].append(y)

check=[-1]*(N+1)
for i in range(1,M+1):
    visit=[0]*(M+1)
    func(i,1)
res=sum(1 for i in check if i!=-1)
plus=0
for i in range(1,M+1):
    copyed=check[:]
    tmp_plus=0
    visit=[0]*(M+3)
    tmp_plus+=func(M+1,i)
    visit=[0]*(M+3)
    tmp_plus+=func(M+2,i)
    plus=max(plus,tmp_plus)
    check=copyed
    if plus==2:
        break
print(res+plus)