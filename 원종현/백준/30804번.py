N=int(input())
li=list(map(int,input().split()))
tmp={}
cnt=0
res=0
idx=0
for i in range(N):
    if li[i] in tmp:
        tmp[li[i]]+=1
    else:
        tmp[li[i]]=1
        cnt+=1

    while cnt>2:
        tmp[li[idx]]-=1
        if not tmp[li[idx]]:
            del tmp[li[idx]]
            cnt-=1
        idx+=1
    res=max(res,i-idx+1)
print(res)