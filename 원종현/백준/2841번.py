import sys
input=sys.stdin.readline

N,P=map(int,input().split())
li=[[0] for _ in range(7)]
res=0
for i in range(N):
    a,b=map(int,input().split())

    while li[a][-1]>b:
        li[a].pop()
        res+=1
    if li[a][-1]==b:
        continue

    li[a].append(b)
    res+=1
print(res)