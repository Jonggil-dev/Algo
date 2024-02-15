N=int(input())
li=list(map(int,input().split()))
dp=[li[0]]

for i in li[1:]:
    if dp[-1]<i:
        dp.append(i)
    else:
        st,end=0,len(dp)-1
        while st<end:
            mid=(st+end)//2
            if dp[mid]<i:
                st=mid+1
            else:
                end=mid
        dp[end]=i
print(len(dp))