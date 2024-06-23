import sys
input=sys.stdin.readline

N,K=map(int,input().split())

parent=[0]*N
color=[0]*N

def find_lca(a,b):
    tmp=set()
    for i in range(1000):
        tmp.add(a)
        a=parent[a]
    for i in range(1000):
        if b in tmp:
            return b
        b=parent[b]
def count_color(a,b):
    colors=set()
    top=find_lca(a,b)
    while top!=a:
        colors.add(color[a])
        a=parent[a]
    while top!=b:
        colors.add(color[b])
        b=parent[b]
    return len(colors)

def fix_color(a,b,val):
    top=find_lca(a,b)
    while top!=a:
        color[a]=val
        a=parent[a]
    while top!=b:
        color[b]=val
        b=parent[b]

for _ in range(K):
    tmp=list(map(int,input().split()))
    r=tmp[0]
    if r==1: #칠하기
        a,b,c=tmp[1:]
        fix_color(a,b,c)
    elif r==2: # 노드변경
        a,b=tmp[1:]
        parent[a]=b
    else: # 사이의 다른 색상 구하기
        a,b=tmp[1:]
        print(count_color(a,b))