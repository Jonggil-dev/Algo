import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=[int(input()) for _ in range(N)]
li.sort()
res=10**11
st,end=0,0
while end<N and st<N:
    gap=li[end]-li[st]
    if gap<M:
        end+=1
    elif gap>=M:
        res=min(res,gap)
        st+=1
print(res)