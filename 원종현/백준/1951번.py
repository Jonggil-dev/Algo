N=int(input())
lN=(len(str(N)))
res=0
tmp,cnt=10**(lN-1),9
for i in range(1,lN+1):
    if i==lN:
        res+=(N-tmp+1)*i
    else:
        res+=cnt*i
        cnt*=10
print(res%1234567)
