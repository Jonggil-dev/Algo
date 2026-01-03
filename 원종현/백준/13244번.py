import sys
input=sys.stdin.readline

def func(x):
    global flag
    for i in li[x]:
        if depth[i]==0:
            depth[i]=depth[x]+1
            func(i)
        elif depth[i]!=0 and abs(depth[x]-depth[i])!=1:
            flag=1
            return

for _ in range(int(input())):
    N=int(input())
    M=int(input())
    flag=0
    li=[set() for _ in range(N+1)]
    depth=[0]*(N+1)
    depth[1]=1
    s=set()
    for i in range(M):
        a,b=map(int,input().split())
        if (a,b) in s or (b,a) in s:
            flag=1
        s.add((a,b))
        s.add((b,a))
        li[a].add(b)
        li[b].add(a)

    if not flag:
        func(1)
    if not flag:
        for i in range(1,N+1):
            if depth[i]==0:
                flag=1
                break
    print('graph' if flag else 'tree')