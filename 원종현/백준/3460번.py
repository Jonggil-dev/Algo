for _ in range(int(input())):
    N=bin(int(input()))[2:]
    for i,j in enumerate(N[::-1]):
        if j=='1':
            print(i,end=" ")