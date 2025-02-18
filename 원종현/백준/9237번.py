N=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
res=-1
for i in range(N):
    res=max(res,li[i]+i+2)
print(res)