import sys
input=sys.stdin.readline
N,M,q=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
for i in range(q):
    query=list(map(int,input().split()))
    if len(query)==4:
        li[query[1]][query[2]]=query[3]
    else:
        li[query[1]],li[query[2]]=li[query[2]],li[query[1]]

for i in range(N):
    print(*li[i])
