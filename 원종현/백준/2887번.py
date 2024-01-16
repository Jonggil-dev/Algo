import sys
input=sys.stdin.readline
N=int(input())
X,Y,Z=[],[],[]
for i in range(N):
    x,y,z=map(int,input().split())
    X.append((x,y,z,i))
    Y.append((x,y,z,i))
    Z.append((x,y,z,i))
X.sort(key=lambda x:x[0])
Y.sort(key=lambda x:x[1])
Z.sort(key=lambda x:x[2])
nodes=[i for i in range(N)]

edges=[]
for i in range(N-1):
    edges.append((abs(X[i][0]-X[i+1][0]),X[i][3],X[i+1][3]))
    edges.append((abs(Y[i][1]-Y[i+1][1]),Y[i][3],Y[i+1][3]))
    edges.append((abs(Z[i][2]-Z[i+1][2]),Z[i][3],Z[i+1][3]))
edges.sort(key=lambda x:x[0])
def find(x):
    if x==nodes[x]:
        return x
    nodes[x]=find(nodes[x])
    return nodes[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b
res=0
for c,a,b in edges:
    if find(a)!=find(b):
        res+=c
        union(a,b)
print(res)