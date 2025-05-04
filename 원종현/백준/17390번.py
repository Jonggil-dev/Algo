import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
li=sorted(list(map(int,input().split())))

for i in range(1,len(li)):
    li[i]=li[i]+li[i-1]
for _ in range(Q):
    L,R=map(int,input().split())
    if L==1:
        print(li[R-1])
    else:
        print(li[R-1]-li[L-2])