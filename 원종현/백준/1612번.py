N=int(input())
if N%2==0 or N%5==0:
    print(-1)
elif N==1:
    print(1)
else:
    c=11
    r=2
    while c%N!=0:
        c=c%N
        c=c*10+1
        r+=1
    print(r)