N=int(input())
li=list(map(int,input().split()))
now=0
res=0
for i in li:
    now=now+1 if now+1<=i else i
    res=max(res,now)
print(res)