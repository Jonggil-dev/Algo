def func(x):
    for i in so:
        for j in so:
            for k in so:
                if i+j+k==x:
                    print(i,j,k)
                    return

so=[]
check=[1]*(1000)
check[0]=0
check[1]=0
for i in range(2,1000):
    if check[i]:
        so.append(i)
    for j in range(i*2,1000,i):
        check[j]=0
for _ in range(int(input())):
    x=int(input())
    func(x)