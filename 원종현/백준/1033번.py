import math

N=int(input())
g=[[] for _ in range(N)]
lcm=1
r=[0]*N
visit=[0]*N

def func(n):
    visit[n]=1
    for i in g[n]:
        next=i[0]
        if not visit[next]:
            r[next]=r[n]*i[2]//i[1]
            func(next)

for i in range(N-1):
    a,b,p,q=map(int,input().split())
    g[a].append((b,p,q))
    g[b].append((a,q,p))
    lcm*=((p*q)//math.gcd(p,q))

r[0]=lcm
func(0)
mgcd=r[0]
for i in range(1,N):
    mgcd=math.gcd(mgcd,r[i])

for i in r:
    print(int(i//mgcd),end=' ')