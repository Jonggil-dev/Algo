import sys
input=sys.stdin.readline

G=int(input())
P=int(input())
r=0
nodes=[i for i in range(G+1)]
def find(x):
    if x==nodes[x]:
        return x
    nodes[x]=find(nodes[x])
    return nodes[x]
def union(x,y):
    x,y,=find(x),find(y)
    nodes[y]=x

res=0
for i in range(P):
    g=int(input())
    now=find(g)
    if not now:
        break
    union(now-1,now)
    res+=1
print(res)
print(nodes)