import sys
input=sys.stdin.readline

N,M=map(int,input().split())
r=[[0]+[-10**9]*M for i in range(N+1)]
l=[[0]+[-10**9]*M for i in range(N+1)]

for i in range(1,N+1):
    tmp=int(input())
    for j in range(1,min(M,(i+1)//2)+1):
        l[i][j]=max(r[i-1][j],l[i-1][j])
        r[i][j]=max(r[i-1][j],l[i-1][j-1])+tmp
    
print(max(r[N][M],l[N][M]))