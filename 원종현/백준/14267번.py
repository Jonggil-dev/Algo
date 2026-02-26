import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def func(now,c):
    for next in tree[now]:
        val=c+tmp[next]
        res[next]+=val
        func(next,val)

N,M=map(int,input().split())
li=[0]+list(map(int,input().split()))
tree=[[] for _ in range(N+1)]
for i in range(2,N+1):
    tree[li[i]].append(i)
tmp=[0]*(N+1)
res=[0]*(N+1)
for _ in range(M):
    i,w=map(int,input().split())
    tmp[i]+=w

func(1,0)
print(*res[1:])