import sys
input=sys.stdin.readline

N,X=map(int,input().split())
li=list(map(int,input().split()))
if max(li)==0:
    print('SAD')
else:
    s=sum(li[:X])
    v=s
    tmp=1
    for i in range(X,N):
        s+=li[i]
        s-=li[i-X]
        if s>v:
            v=s
            tmp=1
        elif s==v:
            tmp+=1
    print(v)
    print(tmp)