N,L=map(int,input().split())
li=list(map(int,input().split()))

tmp=li[-1]
cnt=1
for i in range(N-2,-1,-1):
    if tmp<=(li[i]-L) or tmp>=(li[i]+L):
        print('unstable')
        exit()
    tmp=((tmp*cnt)+li[i])/(cnt+1)
    cnt+=1
print('stable')