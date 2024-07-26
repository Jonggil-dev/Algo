N=int(input())
res=0
for i in range(1,N+1):
    for j in range(i,N+1-i):
        k=N-i-j
        if k>=i+j:
            continue
        else:
            if j>k:
                break
            res+=1
print(res)
