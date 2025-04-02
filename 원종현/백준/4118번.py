while True:
    N=int(input())
    if N==0:
        break
    r={}
    for i in range(N):
        tmp=list(map(int,input().split()))
        for j in tmp:
            if j not in r:
                r[j]=1
    if len(r)==49:
        print("Yes")
    else:
        print("No")