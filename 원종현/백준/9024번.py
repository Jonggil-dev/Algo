import sys

input=sys.stdin.readline


for _ in range(int(input())):
    n,K=map(int,input().split())
    li=sorted(list(map(int,input().split())))
    res=0
    val=200000000
    for i in range(n):
        st=i+1
        end=n-1
        while st<=end:
            mid=(st+end)//2
            tmp=li[i]+li[mid]
            if tmp>K:
                end=mid-1
            else:
                st=mid+1
            if abs(K-tmp)<val:
                res=1
                val=abs(K-tmp)
            elif abs(K-tmp)==val:
                res+=1
    print(res)

