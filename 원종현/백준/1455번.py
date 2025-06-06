import sys
input=sys.stdin.readline

def func(x,y):
    for i in range(x+1):
        for j in range(y+1):
            li[i][j]=0 if li[i][j] else 1

N,M=map(int,input().split())
li=[list(map(int,list(input().strip()))) for _ in range(N)]
res=0

for i in range(N-1,-1,-1):
    for j in range(M-1,-1,-1):
        if li[i][j]:
            res+=1
            func(i,j)
print(res)