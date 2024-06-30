N=int(input())
v=int(input())
li=list(map(int,input().split()))
res=[]
s=[]

for i in range(v):
    if li[i] in res:
        for j in range(len(res)):
            if li[i]==res[j]:
                s[j]+=1
    else:
        if len(res)>=N:
            for j in range(N):
                if s[j]==min(s):
                    del res[j]
                    del s[j]
                    break
        res.append(li[i])
        s.append(1)
res.sort()
print(*res,sep=" ")