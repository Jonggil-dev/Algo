import sys
input=sys.stdin.readline

T=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
Adic,Bdic={},{}
for i in range(n):
    now=A[i]
    if now not in Adic:
        Adic[now]=1
    else:
        Adic[now]+=1
    for j in range(i+1,n):
        now+=A[j]
        if now not in Adic:
            Adic[now]=1
        else:
            Adic[now]+=1
for i in range(m):
    now=B[i]
    if now not in Bdic:
        Bdic[now]=1
    else:
        Bdic[now]+=1
    for j in range(i+1,m):
        now+=B[j]
        if now not in Bdic:
            Bdic[now]=1
        else:
            Bdic[now]+=1
As,Bs=sorted(Adic.keys()),sorted(Bdic.keys())
res=0
for i in range(len(Bs)):
    if T-Bs[i] in Adic:
        res+=Adic[T-Bs[i]]*Bdic[Bs[i]]
print(res)