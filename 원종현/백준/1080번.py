N,M=map(int,input().split())
A=[list(map(int,input())) for _ in range(N)]
B=[list(map(int,input())) for _ in range(N)]

def func(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            A[x][y]=1-A[x][y]

r=0

for a in range(N-2):
    for b in range(M-2):
        if A[a][b]!=B[a][b]:
            r+=1
            func(a,b)
if A!=B:
    print(-1)
else:
    print(r)