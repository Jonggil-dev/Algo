from math import floor

T=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
tmp=list(map(float,input().split()))
new=[0]*T
for i in range(T):
    new[i]=tmp[i]*10
res=0
for i in range(T):
    if tmp[i]>=1:
        res+=floor(li1[i]*new[i]/10)
        res-=li2[i]
    else:
        res+=li1[i]
        res-=floor(li2[i]*new[i]/10)
print(res)