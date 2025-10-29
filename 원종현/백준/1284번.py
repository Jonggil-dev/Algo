while True:
    N=input()
    if N=='0':
        break
    res=len(N)+1
    for i in N:
        if i=='0':
            res+=4
        elif i=='1':
            res+=2
        else:
            res+=3
    print(res)