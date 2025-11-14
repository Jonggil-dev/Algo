N=int(input())
if N==0:
    print('NO')
else:
    while N:
        if N%3>1:
            print('NO')
            exit(0)
        N//=3
    print('YES')