N=int(input())
li=list(map(int,input().split()))
res=0
for i in range(N):
    if li[i]>=li[(i+1)%N]:
        res+=1
print(res)