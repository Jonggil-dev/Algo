N=int(input())
li=list(map(int,input().split()))
r1,r2=0,0
tmp=0
for i in li:
    if i%2==1:
        tmp+=1
    else:
        r1+=tmp
tmp=0
li.reverse()
for i in li:
    if i%2==1:
        tmp+=1
    else:
        r2+=tmp
print(min(r1,r2))