import sys
input=sys.stdin.readline

N=int(input())
res=0
stk=[]
for i in range(N):
    li=list(map(int,input().split()))
    if li[0]==1:
        A,T=li[1],li[2]
        stk.append((A,T))
    if stk:
        s,t=stk.pop()
        t-=1
        if not t:
            res+=s
        else:
            stk.append((s,t))
print(res)