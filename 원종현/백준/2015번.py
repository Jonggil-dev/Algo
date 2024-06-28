N,K=map(int,input().split())
li=list(map(int,input().split()))
dic={}
dic[0]=1
res=0
tmp=0
for i in li:
    tmp+=i
    if (tmp-K) in dic:
        res+=dic[tmp-K]
    if tmp in dic:
        dic[tmp]+=1
    else:
        dic[tmp]=1
print(res)
