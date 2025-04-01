N,L=map(int,input().split())
r,c=1,0
res=0
while c<N:
    if str(L) not in str(r):
        c+=1

    r+=1
print(r-1)