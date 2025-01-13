import sys
input=sys.stdin.readline
N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i>0:
            li[i][j]+=li[i-1][j]
        if j>0:li[i][j]+=li[i][j-1]
        if i>0 and j>0:li[i][j]-=li[i-1][j-1]
res=li[0][0]
for K in range(N):
    for i in range(N-K):
        for j in range(N-K):
            tmp=li[i+K][j+K]
            if i>0:tmp-=li[i-1][j+K]
            if j>0:tmp-=li[i+K][j-1]
            if i>0 and j>0:tmp+=li[i-1][j-1]
            res=max(res,tmp)
print(res)