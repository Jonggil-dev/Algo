S=input()
dp=[0]*(len(S)+1)
dp[1]=1
if len(S)>=2:
    if S[1]!='0' and S[:2]<='34':
        dp[2]=2
    else:
        dp[2]=1
if len(S)>=3:
    for i in range(2,len(S)):
        if S[i-1]!='0' and S[i]!='0' and S[i-1]+S[i]<='34':
            dp[i+1]=dp[i]+dp[i-1]
        elif S[i]!='0':
            dp[i+1]=dp[i]
        else:
            dp[i+1]=dp[i-1]
print(dp[len(S)])