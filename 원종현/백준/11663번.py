import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=list(map(int,input().split()))
li.sort()

def fmin(x):
    st,end=0,N-1
    while st<=end:
        mid=(st+end)//2
        if li[mid]<x:
            st=mid+1
        else:
            end=mid-1
    return end+1

def fmax(x):
    st,end=0,N-1
    while st<=end:
        mid=(st+end)//2
        if x<li[mid]:
            end=mid-1
        else:
            st=mid+1
    return end
for i in range(M):
    a,b=map(int,input().split())
    print(fmax(b)-fmin(a)+1)