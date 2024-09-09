import sys

input=sys.stdin.readline

N,M=map(int,input().split())
name=[]
li=[]

def func(now):
    st=0
    end=N-1
    v=0
    while st<=end:
        mid=(st+end)//2
        if now<=li[mid]:
            v=mid
            end=mid-1
        else:
            st=mid+1

    return v

for i in range(N):
    a,b=input().split()
    name.append(a)
    li.append(int(b))

for i in range(M):
    now=int(input())
    print(name[func(now)])