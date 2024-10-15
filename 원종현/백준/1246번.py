N,M=map(int,input().split())
p=[int(input()) for _ in range(M)]
p.sort()
res=0
val=0
idx=0
for i in range(1,1000001):
    if idx==M:
        break
    while True:
        if idx==M or p[idx]>=i:
            break
        else:
            idx+=1
    if res<min(N,M-idx)*i:
        val=i
        res=min(N,M-idx)*i
print(val,res)