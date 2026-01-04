import sys
input=sys.stdin.readline

def func(x):
    st,end=0,M-1
    while st<=end:
        mid=(st+end)//2
        if li[mid]==x:
            return mid
        elif li[mid]<x:
            st=mid+1
        else:
            end=mid-1
    tmp=[]
    if 0<=st<M:
        tmp.append(st)
    if 0<=end<M:
        tmp.append(end)
    return min(tmp,key=lambda i:(abs(li[i]-x)))

M,N,L=map(int,input().split())
li=sorted(list(map(int,input().split())))
res=0
for i in range(N):
    x,y=map(int,input().split())
    if y>L:
        continue
    tmp=func(x)
    if abs(li[tmp]-x)+y<=L:
        res+=1
    print(x,y,li[func(x)],res)
print(res)