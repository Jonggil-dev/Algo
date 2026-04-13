import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li1,li2=[],[]
for i in range(N):
    a,b=map(int,input().split())
    for j in range(a):
        li1.append(b)
for i in range(M):
    a,b=map(int,input().split())
    for j in range(a):
        li2.append(b)

res=0
for i in range(100):
    res=max(res,li2[i]-li1[i])
print(res)