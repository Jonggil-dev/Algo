N,M=map(int,input().split())
li=list(map(int,input().split()))
dp=[]
for i in range(1,N+1):
    if i not in li:
        dp.append(i)

res=0
tmp=0
for i in dp:
    if tmp:
        res+=min(7,(i-tmp)*2)
    else:
        res+=7
    tmp=i
print(res)