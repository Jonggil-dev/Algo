N=int(input())
dp=[1,1,0,1,1]
for i in range(5,N+1):
    dp.append(0 if dp[i-1]+dp[i-3]+dp[i-4]==3 else 1)
print('SK' if dp[N]==1 else 'CY')
