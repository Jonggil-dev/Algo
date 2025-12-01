import sys
input=sys.stdin.readline


def func(x,g):
    if visit[x]:
        return 0
    visit[x]=1

    for i in li[x]:
        if i in gra[g]:
            continue
        if check[i]==-1 or func(check[i],g):
            check[i]=x
            return 1
    return 0

res=[0]*3
N=int(input())
tmp_gra=input().rstrip()
gra=[[],[],[]] # 2,3 | 1,3 | 1,2
for i in range(N):
    grade=int(tmp_gra[i])-1
    gra[grade].append(i)

tmp=[input().rstrip() for _ in range(N)]
li=[[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if tmp[i][j]=='Y':
            li[i].append(j)

for g in range(3):
    check=[-1]*N
    for i in gra[(g+1)%3]:
        visit=[0]*N
        func(i,g)
    res[g]=N-sum([1 for i in check if i!=-1])
print(max(res))