W,N=map(int,input().split())
A=list(map(int,input().split()))
dp=[0]*(W+1)
A.sort()
r="NO"
c=0
for i in range(N):
    for j in range(i+1,N):
        if A[i]+A[j]<=W:
            dp[A[i]+A[j]]=(i,j)
for i in range(N):
    for j in range(i+1,N):
        if A[i]+A[j]<=W and dp[W-(A[i]+A[j])]:
            if i not in dp[W-(A[i]+A[j])] and j not in dp[W-(A[i]+A[j])]:
                r="YES"
                c=1
                break
    if c:
        break
print(r)