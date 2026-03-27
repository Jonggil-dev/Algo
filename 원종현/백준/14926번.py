from collections import deque
import sys
sys.setrecursionlimit(10**6)
def func(x):
    if len(res)==(N*(N-1))//2:
        return
    while graph[x]:
        y=graph[x].popleft()
        nx,ny=min(x,y),max(x,y)
        if not visit[(nx,ny)]:
            if cnt[y]<N-2:
                visit[(nx,ny)]=1
                cnt[x]+=1
                cnt[y]+=1
                res.append(y)
                func(y)
                break
            else:
                graph[x].append(y)

N=int(input())
visit={}
graph=[deque() for _ in range(N+1)]
cnt=[0]*(N+1)
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            continue
        graph[i].append(j)
        if i<j:
            visit[(i,j)]=0
res=[1,2]
visit[(1,2)]=1
cnt[1]+=1
cnt[2]+=1
func(2)
for i in res:
    print('a',i,sep='',end=' ')
print('a1')