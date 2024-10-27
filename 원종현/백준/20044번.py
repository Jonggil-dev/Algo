N=int(input())
li=sorted(list(map(int,input().split())))
rli=sorted(li,reverse=True)
res=[]
for i in range(N):
    res.append(li[i]+rli[i])
print(min(res))