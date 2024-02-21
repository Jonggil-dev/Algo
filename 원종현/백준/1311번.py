import sys
input=sys.stdin.readline

N=int(input())
D=[list(map(int,input().split()))for _ in range(N)]
dp=[{} for i in range(N)]
for i in range(N):
    dp[0][1<<i]=D[0][i]
#dp[x][101011..]= x번째사람의 일을 결정했을때의 방문상태
for i in range(1,N):
    for status in dp[i-1]:
        for j in range(N):
            if not status&1<<j:
                if status|1<<j not in dp[i]:
                    dp[i][status|1<<j]=dp[i-1][status]+D[i][j]
                else:
                    dp[i][status|1<<j]=min(dp[i][status|1<<j],dp[i-1][status]+D[i][j])
print(dp[N-1][(1<<N)-1])