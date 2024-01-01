N=int(input())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append((a,b))

dp={}
def dis(a,b):
    return (abs(li[a][0]-li[b][0])**2+abs(li[a][1]-li[b][1])**2)**0.5
def dfs(now,visited):
    if visited==(1<<N)-1:
        return dis(now,0)
    if (now,visited) in dp:
        return dp[(now,visited)]
    min_cost=int(1e9)
    for next in range(1,N):
        if visited&(1<<next):
            continue
        cost=dfs(next,visited|(1<<next))+dis(now,next)
        min_cost=min(min_cost,cost)
    dp[(now,visited)]=min_cost
    return min_cost

print(dfs(0,1))