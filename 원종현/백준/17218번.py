A=input()
B=input()
lA,lB=len(A),len(B)
dp=[[0]*(lB+1) for _ in range(lA+1)]

for i in range(lA):
    for j in range(lB):
        if A[i]==B[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

res=''
while dp[lA][lB]!=0:
    if dp[lA][lB]==dp[lA-1][lB]:
        lA-=1
    elif dp[lA][lB]==dp[lA][lB-1]:
        lB-=1
    else:
        res+=A[lA-1]
        lA-=1
        lB-=1
print(res[::-1])