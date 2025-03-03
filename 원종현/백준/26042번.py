import sys
input=sys.stdin.readline

N=int(input())
stk=[]
res=[0,0]
for i in range(N):
    li=list(map(int,input().split()))
    if len(li)==1:
        stk.pop(0)
    else:
        stk.append(li[1])
    if res[0]<len(stk):
        res[0]=len(stk)
        res[1]=stk[-1]
    elif res[0]==len(stk):
        res[1]=min(res[1],stk[-1])
print(*res)