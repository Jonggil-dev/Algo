import sys
input=sys.stdin.readline

def find(x):
    if x!=nodes[x]:
        nodes[x]=find(nodes[x])
    return nodes[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if x>y:
        nodes[x]=y
    else:
        nodes[y]=x

for i in range(int(input())):
    N=int(input())
    nodes=[i for i in range(N+1)]
    K=int(input())
    for j in range(K):
        a,b=map(int,input().split())
        union(a,b)
    M=int(input())
    print(f"Scenario {i+1}:")
    for j in range(M):
        a,b=map(int,input().split())
        print(1 if find(a)==find(b) else 0)
    print()