import sys
input=sys.stdin.readline

N,M=map(int,input().split())
C=[0]+input().split()
nodes=[i for i in range(N+1)]
li=[]
for i in range(M):
    u,v,d=map(int,input().split())
    li.append([u,v,d])
li.sort(key=lambda x:x[2])

def find(a):
    if nodes[a]==a:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

weight=0
count=0
for u,v,d in li:
    if find(u)!=find(v) and C[u]!=C[v]:
        union(u,v)
        weight+=d
        count+=1
print(weight if count==N-1 else -1)