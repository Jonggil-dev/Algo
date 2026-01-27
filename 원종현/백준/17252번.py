N=int(input())
if not N:
    print('NO')
else:
    while N:
        if N%3>1:
            print("NO")
            break
        N//=3
    else:
        print("YES")