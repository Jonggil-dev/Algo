A='0'+input()
B='0'+input()
C='0'+input()
dp=[[[0]*(len(C)) for _ in range(len(B))] for _ in range(len(A))]

for i in range(1,len(A)):
    for j in range(1,len(B)):
        for k in range(1,len(C)):
            if A[i]==B[j]==C[k]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[len(A)-1][len(B)-1][len(C)-1])