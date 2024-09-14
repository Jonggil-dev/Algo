import sys
from itertools import combinations
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
res=0

for a,b,c in combinations(range(M),3):
    tmp=0
    for i in range(N):
        tmp+=max(li[i][a],li[i][b],li[i][c])
    res=max(tmp,res)
print(res)