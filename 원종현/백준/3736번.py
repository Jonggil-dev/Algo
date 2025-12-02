import sys
input=sys.stdin.readline

# pypy3
sys.setrecursionlimit(10**4)
def func(x):
    if visit[x]==idx:
        return 0
    visit[x]=idx

    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0
while True:
    try:
        N=int(input())
        li=[[] for _ in range(N)]
        for _ in range(N):
            S=input().rstrip()
            if len(S)==1:
                continue
            le,ri=S.split(":")
            work=int(le)
            servers=[*map(int,ri.split(")")[1].split())]
            for server in servers:
                li[server-N].append(work)
        check=[-1]*N
        res=0
        visit=[0]*N
        idx=0
        for i in range(N):
            idx+=1
            if func(i):
                res+=1
        print(res)
    except:
        exit()
