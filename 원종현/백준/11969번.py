import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
li=[[0]*(N+1) for _ in range(3)]
for i in range(1,N+1):
    li[int(input())-1][i]=1
res=[[0]*(N+1) for _ in range(3)]
for i in range(3):
    for j in range(1,N+1):
        res[i][j]=res[i][j-1]+li[i][j]

for i in range(Q):
    a,b=map(int,input().split())
    for j in range(3):
        print(res[j][b]-res[j][a-1],end=' ')
    print()