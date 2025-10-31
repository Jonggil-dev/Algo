import sys
input=sys.stdin.readline
d={}
res=0
for _ in range(int(input())):
    x,t,c=map(int,input().split())
    if x-t not in d:
        d[x-t]=c
    else:
        d[x-t]+=c
    res=max(res,d[x-t])
print(res)