N=int(input())
V=2000001
check=[1]*(V)
check[1]=0
for i in range(2,V):
    if check[i]:
        if str(i)[::-1]==str(i) and i>=N:
            print(i)
            break
        for j in range(2*i,V,i):
            check[j]=0