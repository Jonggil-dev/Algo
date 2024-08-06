P,N=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
res=0
for i in li:
    if P<200:
        P+=i
        res+=1
    else:
        break
print(res)