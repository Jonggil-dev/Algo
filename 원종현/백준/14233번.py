def check(t):
    tmp=0
    for i in li:
        tmp+=t
        if i<tmp:
            return 0
    return 1
N=int(input())
li=list(map(int,input().split()))
li.sort()
st,end=1,li[0]
mid=0
res=0
while st<=end:
    mid=(st+end)//2

    if check(mid):
        res=mid
        st=mid+1
    else:
        end=mid-1
print(res)