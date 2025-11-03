import sys
input=sys.stdin.readline

N=int(input())
d={}
for _ in range(N):
    S,W,D,P=input().rstrip().split()
    d[S]=[(int(W)-1)*7+int(D),int(P)]

li=[0]*(70)
for _ in range(N):
    S,M=input().rstrip().split()
    if d[S][1]<=int(M):
        li[d[S][0]]=1

res=0
tmp=0
for i in li:
    if i:
        tmp+=1
    else:
        res=max(res,tmp)
        tmp=0
res=max(res,tmp)
print(res)