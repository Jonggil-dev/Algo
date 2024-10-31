N=int(input())
dic={}
for _ in range(N):
    a,b=map(int,input().split())
    if not b in dic:
        dic[b]=[a]
    else:
        dic[b].append(a)
res=0
for i in dic.values():
    i.sort()
    if len(i)<=1:
        continue
    res+=abs(i[0]-i[1])+abs(i[-1]-i[-2])
    for j in range(1,len(i)-1):
        res+=min(abs(i[j]-i[j-1]),abs(i[j]-i[j+1]))
print(res)