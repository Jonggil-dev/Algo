import math
N=int(input())
li=[]
check=[0]*N
for i in range(N):
    li.append(int(input()))
K=int(input())
dp=[[0]*K for _ in range(1<<N)] # dp[i][j] =i(1011) 순열을 사용할 때 나머지가 j인 경우의 수
dp[0][0]=1

val=[]
for l in range(N):
    tmp=[]
    for j in range(K):
        tmp.append((j*(10**(len(str(li[l])))%K)+(li[l]%K))%K)
    val.append(tmp)
for i in range(1<<N):
    for l in range(N):
        if i&(1<<l):
            continue
        for j in range(K):
            next=val[l][j]
            dp[i|(1<<l)][next]+=dp[i][j]
p=dp[(1<<N)-1][0]
q=sum(dp[(1<<N)-1])
g=math.gcd(p,q)
print(f'{p//g}/{q//g}')