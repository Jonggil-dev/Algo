import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def func(x):
    if visit[x]==idx:
        return 0
    visit[x]=idx
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

for _ in range(int(input())):
    H,V=map(int,input().split())
    d={}
    li=[[] for _ in range(H)]
    for i in range(H):
        x,y,W=input().rstrip().split()
        x=int(x)
        y=int(y)
        for j in range(x,x+len(W)):
            d[(j,y)]=(W[j-x],i)
    for i in range(V):
        x,y,W=input().rstrip().split()
        x=int(x)
        y=int(y)
        for j in range(y,y+len(W)):
            if (x,j) in d and d[(x,j)][0]!=W[j-y]:
                li[d[(x,j)][1]].append(i)

    idx=0
    check=[-1]*V
    visit=[0]*H
    for i in range(H):
        idx+=1
        func(i)
    print(H+V-sum([1 for i in check if i!=-1]))