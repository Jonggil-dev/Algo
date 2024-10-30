import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
V,E=map(int,input().split())
li=[]
cnt=0
weight=0
nodes=[i for i in range(V+1)]
for i in range(E):
    A,B,C=map(int,input().split()) # A와 B가 가중치 C로 연결
    li.append([A,B,C])

def find(a):
    if nodes[a]==a:
        return a
    else:
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
li.sort(key=lambda x:x[2]) # 가중치 오름차순으로 정렬
i=0
while cnt<V-1:
    a,b,v=li[i][0],li[i][1],li[i][2]
    if find(a)!=find(b):
        cnt+=1
        weight+=v
        union(a,b)
    i+=1
print(weight)
