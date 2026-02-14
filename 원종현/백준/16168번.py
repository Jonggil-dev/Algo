import sys
input=sys.stdin.readline

def find(a):
    if nodes[a]==a:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        nodes[b]=a
    else:
        nodes[a]=b

V,E=map(int,input().split())
nodes=[i for i in range(V+1)]
graph=[[] for _ in range(V+1)]
for _ in range(E):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    if find(v1)!=find(v2):
        union(v1,v2)

st=find(1)
for i in range(2,V+1):
    if st!=find(i):
        print('NO')
        exit()

cnt=0
for i in range(1,V+1):
    if len(graph[i])%2==1:
        cnt+=1
if cnt==2 or cnt==0:
    print('YES')
else:
    print('NO')