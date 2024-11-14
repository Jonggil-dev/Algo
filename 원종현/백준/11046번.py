import sys
input=sys.stdin.readline
N=int(input())
S=['#']*(2*N+1)
tmp=list(input().split())
for i in range(N):
    S[i*2+1]=tmp[i]
res=0
li=[0]*(len(S))
r,p=0,0
for i in range(len(S)):
    if i<=r:
        li[i]=min(li[2*p-i],r-i)
    while i-li[i]-1>=0 and i+li[i]+1<len(S) and S[i-li[i]-1]==S[i+li[i]+1]:
        li[i]+=1
    if r<i+li[i]:
        r=i+li[i]
        p=i
    res+=(li[i]+1)//2
for i in range(int(input())):
    A,B=map(lambda x:int(x)-1,input().split())
    if li[A+B+1]>=B-A+1:
        print(1)
    else:
        print(0)
    pass