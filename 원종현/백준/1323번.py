N,K=map(int,input().split())
r=0
tmp=N
check=set()
while True:
    tmp=tmp%K
    r+=1
    if tmp==0:
        break
    else:
        tmp=int(str(tmp)+str(N))
        if tmp in check:
            r=-1
            break
        check.add(tmp)
print(r)