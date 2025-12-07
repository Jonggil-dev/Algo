N=int(input())
li=list(map(int,input().split()))
res=0
for i in range(N-1):
    res+=(li[i]*li[i+1])
    li[i+1]=li[i]+li[i+1]
print(res)