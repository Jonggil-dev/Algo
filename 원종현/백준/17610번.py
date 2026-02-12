K=int(input())
li=list(map(int,input().split()))
li.sort()
tot=sum(li)
tmp_li=[li[0]]
for i in range(1,K):
    now=li[i]
    tmp=[now]
    for j in tmp_li:
        tmp+=[now+j,abs(now-j)]
    tmp_li+=tmp
tmp_li=list(set(tmp_li))
if 0 in tmp_li:
    tmp_li.remove(0)
print(tot-len(tmp_li))