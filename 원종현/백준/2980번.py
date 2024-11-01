N,L=map(int,input().split())
li=[]
res=0
now=0
for i in range(N):
    D,R,G=map(int,input().split())
    res+=(D-now)
    now=D
    if res%(R+G)<=R:
        res+=(R-(res%(R+G)))
res+=(L-now)
print(res)