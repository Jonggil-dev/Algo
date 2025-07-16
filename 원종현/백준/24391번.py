import sys
input=sys.stdin.readline

def find(a):
    if a!=nodes[a]:
        nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        nodes[a]=b
    else:
        nodes[b]=a

N,M=map(int,input().split())
nodes=[i for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    union(a,b)

li=list(map(int,input().split()))
res=0
for i in range(1,len(li)):
    if find(li[i-1])!=find(li[i]):
        res+=1
print(res)