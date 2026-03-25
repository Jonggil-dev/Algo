import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
li=[input().rstrip() for _ in range(N)]
res=0
for i in range(N):
    tmp=1
    for j in range(M):
        if li[i][j]=='0':
            if tmp>=K:
                res+=1
            tmp+=1
        else:
            tmp=1
print(res)