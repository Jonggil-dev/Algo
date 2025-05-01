import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    res=0
    for i in A:
        st,end=0,len(B)-1
        tmp=-1
        while st<=end:
            mid=(st+end)//2
            if B[mid]<i:
                tmp=mid
                st=mid+1
            else:
                end=mid-1
        res+=tmp+1
    print(res)