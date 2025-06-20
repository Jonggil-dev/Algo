N,X=map(int,input().split())

if N>X or N*26<X:
    print('!')
else:
    tmp=['A']*N
    X-=N
    idx=N-1
    while X>0:
        if X>=25:
            tmp[idx]='Z'
            idx-=1
            X-=25
        else:
            tmp[idx]=chr(X+65)
            break
    print(''.join(tmp))