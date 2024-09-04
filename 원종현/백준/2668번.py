import sys
input=sys.stdin.readline
N=int(input())
graph=[[] for _ in range(N+1)]
for i in range(1,N+1):
    graph[i].append(int(input()))
res=[]
def func(n):
    global res

    visit[n]=True
    for now in graph[n]:
        if not visit[now]:
            func(now)
        elif visit[now] and not finish[now]:
            if now not in res:
                res.append(now)
                return
        else:
            return
    finish[n]=1


for i in range(1,N+1):
    visit=[0]*(N+1)
    finish=[0]*(N+1)
    func(i)

res.sort()
print(len(res))
for i in res:
    print(i)