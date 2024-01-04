N,M,K=map(int,input().split())
candy=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
res=0
bac=[]
visit=[0]*(N+1)
for i in range(1,N+1):
    if not visit[i]:
        tmp=[candy[i],1]
        visit[i]=1
        q=[i]
        while q:
            now=q.pop()
            for j in graph[now]:
                if not visit[j]:
                    tmp[0]+=candy[j]
                    tmp[1]+=1
                    visit[j]=1
                    q.append(j)
        bac.append(tmp)
dp=[0]*(K+1)
bac.sort(key=lambda x:x[1])
for v,i in bac:
    for idx in range(K,i-1,-1):
        dp[idx]=max(dp[idx-i]+v,dp[idx])
print(dp[K-1])