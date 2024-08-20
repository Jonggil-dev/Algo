import sys
input=sys.stdin.readline

N=int(input())
x1,x2=500,0
y1,y2=500,0
li=[[0]*501 for _ in range(501)]
res=0
for i in range(N):
    X1,Y1,X2,Y2=map(int,input().split())
    x1=min(x1,X1)
    x2=max(x2,X2)
    y1=min(y1,Y1)
    y2=max(y2,Y2)
    for j in range(X1,X2):
        for k in range(Y1,Y2):
            li[k][j]=1
for i in range(x1,x2):
    for j in range(y1,y2):
        if li[j][i]:
            res+=1
print(res)