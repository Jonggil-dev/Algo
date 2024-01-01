import sys
input=sys.stdin.readline
N=int(input())
li=[]
dp={}
for i in range(N):
    li.append(list(map(int,input().split())))

def dfs(now,visited):
    if visited==(1<<N)-1:
        if li[now][0]:
            return li[now][0]
        else:
            return int(1e9)

    if (now,visited) in dp:
        return dp[(now,visited)]

    min_val=int(1e9)
    for next in range(1,N):
        if li[now][next]==0 or visited&(1<<next):
            continue
        cost=dfs(next,visited|(1<<next))+li[now][next]
        min_val=min(min_val,cost)

    dp[(now,visited)]=min_val
    return min_val

print(dfs(0,1))