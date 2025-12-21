N=int(input())
li=list(map(int,input().split()))
li.sort()
res=N
tmp=1
for i in li:
    if tmp+i>=res:
        break
    else:
        tmp+=i
        res-=1
print(res-1)