
N=int(input())
li=list(map(int,input().split()))
li.sort()

res=li[-1]
if N%2==1:
    for i in range(N//2):
        tmp=li[i]+li[N-i-2]
        res=max(res,tmp)
else:
    for i in range(N//2):
        tmp=li[i]+li[N-i-1]
        res=max(res,tmp)
print(res)