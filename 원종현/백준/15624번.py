N=int(input())

before,after=0,1
idx=1
if N==0:
    print(0)
else:
    while idx!=N:
        tmp=after
        after=(before+tmp)%1000000007
        before=tmp%1000000007
        idx+=1
    print(after)