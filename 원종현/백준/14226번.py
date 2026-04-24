from collections import deque
S=int(input())
dp=[[-1]*(S+1) for _ in range(S+1)]
dp[1][0]=0

q=deque()
q.append((1,0))
while q:
    now,c=q.popleft()
    if dp[now][now]==-1:
        dp[now][now]=dp[now][c]+1
        q.append((now,now))
    if now+c<=S and dp[now+c][c]==-1:
        dp[now+c][c]=dp[now][c]+1
        q.append((now+c,c))
    if now-1>=0 and dp[now-1][c]==-1:
        dp[now-1][c]=dp[now][c]+1
        q.append((now-1,c))

res=10**9
for i in range(S+1):
    if dp[S][i]!=-1:
        res=min(dp[S][i],res)

print(res)