N,M=map(int,input().split())
so=[]
check=[1]*(M-N+1)
for i in range(2,int(M**0.5)+1):
    now=(N//(i**2))*(i**2)
    while now<M+1:
        if now-N>=0:
            check[now-N]=0
            print(now-N)
        now+=(i**2)
print(sum(check))