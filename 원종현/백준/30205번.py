N,M,P=map(int,input().split())
for i in range(N):
    li=list(map(int,input().split()))
    li.sort()
    tmp=li.count(-1)
    tmp2=tmp
    for j in li[tmp2:]:
        if j>P:
            while j>P:
                if tmp>=1:
                    tmp-=1
                    P*=2
                else:
                    print(0)
                    exit()
            P+=j
        else:
            P+=j
    while tmp:
        tmp-=1
        P*=2
print(1)