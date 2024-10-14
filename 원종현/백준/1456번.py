A,B=map(int,input().split())
so=[]
check=[1]*(int(B**0.5)+1)
check[1]=0
for i in range(2,int(B**0.5)+1):
    if check[i]:
        so.append(i)
        for j in range(i**2,int(B**0.5)+1,i):
            check[j]=0
res=0
for i in so:
    now=i*i
    while True:
        if now<A:
            now*=i
            continue
        if now>B:
            break
        res+=1
        now*=i
print(res)