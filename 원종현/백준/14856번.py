
N=int(input())
MAX=95
dp=[1,2]

while True:
    if dp[-1]>N:
        break
    dp.append(dp[-1]+dp[-2])
res=[]
while dp:
    v=dp.pop()
    if v<=N:
        res.append(v)
        N-=v

if res:
    print(len(res))
    print(*res[::-1])
else:
    print(-1)