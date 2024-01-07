S=input()
dp=[[0]*len(S) for _ in range(len(S))]
for i in range(len(S)):
    dp[i][i]=1
for i in range(1,len(S)):
    if S[i-1]==S[i]:
        dp[i-1][i]=1
for i in range(3,len(S)+1):
    for st in range(len(S)-i+1):
        end=st+i-1
        if S[st]==S[end] and dp[st+1][end-1]:
            dp[st][end]=1

res=[10**9]*(len(S)+1)
res[len(S)]=0
for end in range(len(S)):
    for st in range(end+1):
        if dp[st][end]:
            res[end]=min(res[end],res[st-1]+1)
        else:
            res[end]=min(res[end],res[end-1]+1)
print(res[len(S)-1])
