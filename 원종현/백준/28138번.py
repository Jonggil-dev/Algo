N,R=map(int,input().split())

res=0
P=N-R
for i in range(1,int(P**(1/2))+1):
    if P%i==0:
        if i>R:
            res+=i
        if i*i!=P and P//i>R:
            res+=P//i
print(res)