from collections import deque
import sys
input=sys.stdin.readline

def get_distance(a,b):
    dist=(((graph[a][0]-graph[b][0]))**2+((graph[a][1]-graph[b][1]))**2)**0.5
    return int(dist//10)+1 if dist%10 else dist//10

def check(x):
    visit=set()
    visit.add(0)
    q=deque([(0,0)])
    while q:
        now,c=q.popleft()
        if dist[now][N+1]<=x:
            return 1
        for i in range(N+2):
            if i not in visit and dist[now][i]<=x and c+1<=K:
                visit.add(i)
                q.append((i,c+1))
    return 0
N,K=map(int,input().split())
st,end=[0,0],[10000,10000]
graph=[[0,0]]+[list(map(int,input().split())) for _ in range(N)]+[[10000,10000]]
dist=[[0]*(N+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        dist[i][j]=get_distance(i,j)

st,end=0,dist[0][N+1]
res=end
while st<=end:
    mid=(st+end)//2
    if check(mid):
        res=mid
        end=mid-1
    else:
        st=mid+1
print(res)
