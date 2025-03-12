N=int(input())
li=list(map(int,input().split()))
li.sort()
tmp1,tmp2=0,0
for i in range(N//2):
    tmp2+=li[i]
tmp1=sum(li)-tmp2
print(tmp2,tmp1)