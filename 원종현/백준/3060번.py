for _ in range(int(input())):
    N=int(input())
    s=sum(list(map(int,input().split())))
    tmp=1
    while N>=s:
        tmp+=1
        s*=4
    print(tmp)