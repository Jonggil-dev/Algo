import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
li=list(map(int,input().split()))
li.sort()
l,r=0,len(li)-1
res=0
while l<r:
    tmp=li[l]+li[r]
    if tmp<M:
        l+=1
    elif tmp>M:
        r-=1
    else:
        res+=1
        l+=1
        r-=1
print(res)