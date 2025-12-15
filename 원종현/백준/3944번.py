for _ in range(int(input())):
    B,D=input().split()
    B=int(B)
    res=0
    for i in range(len(D)):
        res+=int(D[i])
    print(res%(B-1))