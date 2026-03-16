import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
poisons=set(list(map(int,input().split())))
li=[list(map(int,input().split())) for i in range(M)]
li.sort(key=lambda x:x[0])

for c in range(1,N+1):
    tmp=set()
    tmp.add(c)
    for i,a,b in li:
        if a in tmp:
            tmp.add(b)
    if tmp==poisons:
        print(c)
        break