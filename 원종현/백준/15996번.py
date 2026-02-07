N,A=map(int,input().split())
res=0
tmp=A
while tmp<=N:
    res+=N//tmp
    tmp*=A
print(res)