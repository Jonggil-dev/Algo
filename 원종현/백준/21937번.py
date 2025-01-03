import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N,M=map(int,input().split())
graph=[[]for _ in range(N+1)]
visit=[0]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    graph[b].append(a)
X=int(input())
res=0
def func(x):
    global res
    visit[x]=1
    for i in graph[x]:
        if not visit[i]:
            res+=1
            func(i)
func(X)
print(res)