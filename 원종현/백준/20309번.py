N=int(input())
li=list(map(int,input().split()))
res=1
for i in range(N):
    if i%2 and li[i]%2:
        res=0
        break
print('YES' if res else 'NO')