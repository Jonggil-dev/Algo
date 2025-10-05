import sys
input=sys.stdin.readline
L,N,rF,rB=map(int,input().split())
li=[]
for i in range(N):
    x,c=input().split()
    li+=[(int(x),int(c))]

res,max_v=0,0
for i in sorted(li,key=lambda x:x[1],reverse=True):
    x,c=i
    if x<max_v:
        continue
    res+=(x-max_v)*(rF-rB)*c
    max_v=x
print(res)