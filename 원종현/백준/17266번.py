import sys

input=sys.stdin.readline

N=int(input())
M=int(input())
li=list(map(int,input().split()))

res=0
if M==1:
    res=max(li[0],N-li[0])
else:
    for i in range(M):
        if i==0:
            res=max(res,li[i])
        elif i==M-1:
            res=max(res,N-li[i])
        else:
            tmp=li[i]-li[i-1]
            if tmp%2:
                res=max(res,tmp//2+1)
            else:
                res=max(res,tmp//2)
print(res)