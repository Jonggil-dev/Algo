import sys
input=sys.stdin.readline

N,K,Q,M=map(int,input().split())
li=[0]*(N+3)
for i in map(int,input().split()):
    li[i]=1

chk=[1]*(N+3)
for i  in map(int,input().split()):
    if li[i]:
        continue
    for j in range(i,N+3,i):
        if li[j]:
            continue
        chk[j]=0

tmp=0
chk[2]=0
for i in range(3,N+3):
    if chk[i]:
        tmp+=1
    chk[i]=tmp
for i in range(M):
    s,e=map(int,input().split())
    print(chk[e]-chk[s-1])