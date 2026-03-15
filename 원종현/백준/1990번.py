
a,b=map(int,input().split())

def func(x):
    st=str(x)
    for i in range(len(st)):
        if st[i]!=st[len(st)-1-i]:
            return 0
    return 1


for i in range(a,min(b+1,10000000)):
    f=1
    if func(i):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                f=0
                break
        if f:
            print(i)
print(-1)