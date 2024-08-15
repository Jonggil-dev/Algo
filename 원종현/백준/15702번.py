import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=list(map(int,input().split()))
r1=0
r2=100001
for i in range(M):
    tmp=list(input().split())
    count=0
    for j in range(1,N+1):
        if tmp[j]=='O':
            count+=int(li[j-1])
    if r1<count:
        r1=count
        r2=int(tmp[0])
    elif r1==count:
        r2=min(r2,int(tmp[0]))
print(r2,r1)
