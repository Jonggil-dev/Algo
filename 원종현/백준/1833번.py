import sys
input=sys.stdin.readline

def find(a):
    if nodes[a]==a:
        return a
    else:
        nodes[a]=find(nodes[a])
        return nodes[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

N=int(input())
nodes=[i for i in range(N+1)]
weight=0
tmp=[list(map(int,input().split())) for _ in range(N)]
li=[]
for i in range(N):
    for j in range(i+1,N):
        if tmp[i][j]>0:
            li.append((i,j,tmp[i][j]))
        elif tmp[i][j]<0:
            union(i,j)
            weight-=tmp[i][j]
li.sort(key=lambda x:x[2])
cnt,res=0,[]
for a,b,v in li:
    if find(a)!=find(b):
        weight+=v
        union(a,b)
        cnt+=1
        res.append((a+1,b+1))
print(weight,cnt)
for a,b in res:
    print(a,b)
