import sys

input=sys.stdin.readline
R,C=map(int,input().split())
li=[]
d=[[[0]*2 for _ in range(C)]  for _ in range(R)]
u=[[[0]*2 for _ in range(C)]  for _ in range(R)]

for i in range(R):
    tmp=input().rstrip()
    for j in range(C):
        if tmp[j]=="1":
            d[i][j][0]=1
            d[i][j][1]=1
            u[i][j][0]=1
            u[i][j][1]=1
    li.append(tmp)

for i in range(R-1,-1,-1):
    for j in range(C):
        if li[i][j]=="1":
            if 0<=i+1<R and 0<=j-1<C:
                d[i][j][0]=d[i+1][j-1][0]+1
            if 0<=i+1<R and 0<=j+1<C:
                d[i][j][1]=d[i+1][j+1][1]+1
for i in range(R):
    for j in range(C):
        if li[i][j]=="1":
            if 0<=i-1<R and 0<=j-1<C:
                u[i][j][0]=u[i-1][j-1][0]+1
            if 0<=i-1<R and 0<=j+1<C:
                u[i][j][1]=u[i-1][j+1][1]+1
res=0

for i in range(R):
    for j in range(C):
        tmp=0
        d_min=min(d[i][j])
        if d_min!=0 and d_min>res:
            k=1
            while k<=d_min*2-1 and i+k-1<R:
                tmp=max(tmp,k//2+1 if min(u[i+k-1][j])>=k//2+1 else 0)
                k+=2
        res=max(res,tmp)
print(res)