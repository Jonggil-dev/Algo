import sys
input=sys.stdin.readline

def get_distance(p):
    tmp=[0]*N
    for i in range(N):
        tmp[i]=sum([abs(j-p[i]) for j in P[i]])
    return sum(tmp)
N,M=map(int,input().split())
P=[[0]*M for _ in range(N)]
for i in range(M):
    tmp=list(map(int,input().split()))
    for j in range(N):
        P[j][i]=tmp[j]
for i in P:
    i.sort()

p=[P[i][M//2] for i in range(N)]
print(get_distance(p))
print(*p)