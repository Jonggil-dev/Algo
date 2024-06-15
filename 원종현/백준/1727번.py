import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
if N>M:
    li1,li2=li2,li1
    N,M=M,N
dp=[[0]*M for i in range(N)]
li1.sort()
li2.sort()
dp[0][0]=abs(li1[0]-li2[0])
for i in range(1,M-(N-1)):
    dp[0][i]=min(abs(li1[0]-li2[i]),dp[0][i-1])

for i in range(1,N):
    for j in range(i,M-(N-i-1)):
        if i==j:
            dp[i][j]=dp[i-1][j-1]+abs(li1[i]-li2[j])
        else:
            dp[i][j]=min(dp[i-1][j-1]+abs(li1[i]-li2[j]),dp[i][j-1])
print(dp[N-1][M-1])