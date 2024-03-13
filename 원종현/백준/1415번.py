N=int(input())
candy={}
tot=0
for i in range(N):
    now=int(input())
    tot+=now
    if now in candy:
        candy[now]+=1
    else:
        candy[now]=1

dp=[[0]*(tot+1) for _ in range(len(candy)+1)]

so_v=[1]*(tot+1)
so=set()
for i in range(2,int(tot**0.5)+1):
    if so_v[i]:
        for j in range(i+i,tot+1,i):
            so_v[j]=0
for i in range(2,tot+1):
    if so_v[i]:
        so.add(i)
res=0
c=1
dp[0][0]=1

for k,v in candy.items():
    for i in range(tot+1):
        dp[c][i]=dp[c-1][i]
        for j in range(1,v+1):
            if i-j*k<0:break
            dp[c][i]+=dp[c-1][i-j*k]

    c+=1
for i in so:
    res+=dp[len(candy)][i]

print(res)