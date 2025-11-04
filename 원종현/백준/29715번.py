import math
N,M=map(int,input().split())
X,Y=map(int,input().split())
cnt1,cnt2=0,0
for i in range(M):
    a,b=map(int,input().split())
    if a!=0:
        cnt1+=1
    else:
        cnt2+=1
N-=cnt1
res=1
if cnt2>0:
    res*=math.comb(N,cnt2)*math.factorial(cnt2)
N-=cnt2
if N>0:
    res*=math.perm(9-(cnt1+cnt2),N)
print(res*X+((res-1)//3)*Y)