import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append(b)
li.append(0)
res=0
stk=[0]
for i in li:
    h=i
    while stk[-1]>i:
        if stk[-1]!=h:
            res+=1
            h=stk[-1]
        stk.pop()
    stk.append(i)
print(res)