import sys
input=sys.stdin.readline


def func(x):
    if x in visit:
        return 0
    visit[x]=1
    for i in d[x]:
        if i not in check or func(check[i]):
            check[i]=x
            return 1
    return 0

N,M=map(int,input().split())
s,c=set(),set()
for _ in range(N):
    a,b=input().split()
    a=int(a)
    if b=='s':
        s.add(a)
    else:
        c.add(a)
d={}
for _ in range(M):
    a,b=map(int,input().split())
    if a in c:
        if a in d:
            d[a].append(b)
        else:
            d[a]=[b]
    else:
        if b in d:
            d[b].append(a)
        else:
            d[b]=[a]
check={}
for i in d.keys():
    visit={}
    func(i)
print(N-len(check))

