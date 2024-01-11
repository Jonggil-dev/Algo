import sys
input = sys.stdin.readline

N,M,K=map(int,input().split())
plant=list(map(int,input().split()))
graph=[]
nodes=[i for i in range(N+1)]
for _ in range(M):
    graph.append(list(map(int,input().split())))
graph.sort(key = lambda x:x[2])

def find(a):
    if nodes[a]==a:
        return a
    else:
        nodes[a]=find(nodes[a])
        return nodes[a]

def union(a,b):
    if a not in plant and b in plant:
        nodes[a]=b
    elif a in plant and b not in plant:
        nodes[b]=a
    else:
        if a<b:
            nodes[a]=b
        else:
            nodes[b]=a
res=0
for a,b,c in graph:
    A=find(a)
    B=find(b)
    if A!=B and (A not in plant or B not in plant):
        union(A,B)
        res+=c

print(res)
