N,M,T=map(int,input().split())

r,v=0,10**9

for i in range(T//N+1):
    j=(T-i*N)//M
    print('@',i,j)
    c=T-(i*N+j*M)
    if c<v:
        v=c
        r=i+j
    elif c==v:
        r=max(r,i+j)
print(r,v)