import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[0]*(N+1) for _ in range(N+1)]
cnt=[0]*(N+1)
for _ in range(M):
    A,B=map(int,input().split())
    graph[A][B]=1
    graph[B][A]=1
    cnt[A]+=1
    cnt[B]+=1

res=100000

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if not graph[i][j]:
            continue
        for k in range(j+1,N+1):
            if not graph[i][k] or not graph[j][k]:
                continue
            res=min(res,cnt[i]+cnt[j]+cnt[k]-6)
print(-1 if res==100000 else res)