import sys
input=sys.stdin.readline

N,M=map(int,input().split())
S=[input().rstrip() for i in range(N)]
d={}
for i in S:
    for j in range(1,len(i)+1):
        if i[:j] not in d:
            d[i[:j]]=1
res=0
for i in range(M):
    now=input().rstrip()
    if now in d:
        res+=1
print(res)