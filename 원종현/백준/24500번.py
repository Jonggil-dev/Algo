N=int(input())
a=1
while a<N:
    a=a*2+1
if N==a:
    print(1)
    print(N)
else:
    print(2)
    print(N^a,N,sep="\n")