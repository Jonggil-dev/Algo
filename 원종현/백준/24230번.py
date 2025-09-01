import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def func(fir,next):
    global cnt
    visit[next]=1
    if li[fir]!=li[next]:
        cnt+=1
    for i in graph[next]:
        if not visit[i]:
            func(next,i)

N=int(input())
li=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0
visit=[0]*(N+1)

func(0,1)
print(cnt)