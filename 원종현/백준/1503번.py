N,M=list(map(int,input().split()))
li=list(map(int,input().split()))
res=10**9
for i in range(1,1002):
    if i in li:
        continue
    for j in range(1,1002):
        if j in li:
            continue
        for k in range(1,1002):
            if k in li:
                continue
            tmp=i*j*k
            if abs(N-tmp)<res:
                res=abs(N-tmp)
            if N+1<tmp:
                break
print(res)