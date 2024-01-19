import sys
input=sys.stdin.readline
N=int(input())
r=[-1,0]
for i in range(N):
    g=list(map(int,input().split()))
    t=-1
    for x in range(3):
        for y in range(x+1,4):
            for z in range(y+1,5):
                t=max(t,(g[x]+g[y]+g[z])%10)
    if r[0]<=t:
        r=[t,i+1]
print(r[1])