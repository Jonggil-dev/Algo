T=input()
P=input()
N,M=len(T),len(P)
dp=[0]*(M)
idx=0
for i in range(1,M):
    while idx>0 and P[i]!=P[idx]:
        idx=dp[idx-1]
    if P[i]==P[idx]:
        idx+=1
        dp[i]=idx
idx=0
r=0
loc=[]
for i in range(N):
    while idx>0 and T[i]!=P[idx]:
        idx=dp[idx-1]
    if T[i]==P[idx]:
        if idx==(M-1):
            r+=1
            loc.append(i-M+2)
            idx=dp[idx]
        else:
            idx+=1

print(r)
print(*loc)