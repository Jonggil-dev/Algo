for _ in range(int(input())):
    G=int(input())
    li=[int(input()) for _ in range(G)]
    res=0
    while True:
        res+=1
        if len({i%res for i in li})==G:
            print(res)
            break