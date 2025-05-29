from collections import deque
import sys
input=sys.stdin.readline
d=[(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
N,M,K=map(int,input().split())
li=[[5]*(N+1) for _ in range(N+1)]
A=[[0]*(N+1)]+[[0]+list(map(int,input().split()))for _ in range(N)]
tree=[[deque() for _ in range(N+1)] for _ in range(N+1)]
dead=[]
for _ in range(M):
    x,y,z=map(int,input().split())
    tree[x][y].append(z)

idx=0
while idx<K:
    for i in range(4):
        if i==0:
            for x in range(1,N+1):
                for y in range(1,N+1):
                    if tree[x][y]:
                        length=len(tree[x][y])
                        for k in range(length):
                            if tree[x][y][k]<=li[x][y]:
                                li[x][y]-=tree[x][y][k]
                                tree[x][y][k]+=1
                            else:
                                for _ in range(k,length):
                                    dead.append((tree[x][y].pop(),x,y))
                                break
        elif i==1:
            while dead:
                z,x,y=dead.pop()
                li[x][y]+=z//2
        elif i==2:
            for x in range(1,N+1):
                for y in range(1,N+1):
                    if tree[x][y]:
                        for k in range(len(tree[x][y])):
                            if tree[x][y][k]%5==0:
                                for dx,dy in d:
                                    nx,ny=x+dx,y+dy
                                    if 1<=nx<=N and 1<=ny<=N:
                                        tree[nx][ny].appendleft(1)
        else:
            for x in range(1,N+1):
                for y in range(1,N+1):
                    li[x][y]+=A[x][y]
    idx+=1
res=0
for x in range(1,N+1):
    for y in range(1,N+1):
        res+=len(tree[x][y])
print(res)
