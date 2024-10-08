code=list(map(int,input()))
dp=[0]*(len(code)+1)
dp[0]=1
dp[1]=1
if code[0]==0:
    print(0)
else:
    for i in range(1,len(code)):
        if code[i]>0:
            dp[i+1]+=dp[i]
        if 10<=code[i-1]*10+code[i]<=26:
            dp[i+1]+=dp[i-1]
    print(dp[len(code)]%1000000)