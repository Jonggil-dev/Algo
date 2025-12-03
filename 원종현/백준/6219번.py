A,B,D=map(int,input().split())
li=[1]*(B+1)
for i in range(2,int(B**0.5)+1):
    if li[i]:
        for j in range(i*2,B+1,i):
            li[j]=0
so=[i for i in range(A,B+1) if li[i]]
res=0
for i in so:
    if str(D) in str(i):
        res+=1
print(res)