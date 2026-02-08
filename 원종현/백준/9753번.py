n=50000
check=[0,0]+[1]*(n-1)
so=[]
for i in range(2,n+1):
    if check[i]:
        so.append(i)
        for j in range(2*i,n+1,i):
            check[j]=0

tmp=[]

for i in so:
    for j in so:
        if i!=j and i*j<=100001:
            tmp.append(i*j)
tmp.sort()

for i in range(int(input())):
    K=int(input())
    for j in tmp:
        if j>=K:
            print(j)
            break