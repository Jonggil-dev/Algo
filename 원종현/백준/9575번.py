N=int(input())
for _ in range(N):
    A=int(input())
    liA=list(map(int,input().split()))
    B=int(input())
    liB=list(map(int,input().split()))
    C=int(input())
    liC=list(map(int,input().split()))
    res=[]
    for a in liA:
        for b in liB:
            for c in liC:
                tmp=str(a+b+c)
                flag=1
                for i in tmp:
                    if i=='5' or i=='8':
                        pass
                    else:
                        flag=0
                        break
                if flag and int(tmp) not in res:
                    res.append(int(tmp))
    print(len(res))