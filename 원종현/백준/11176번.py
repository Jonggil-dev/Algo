for _ in range(int(input())):
    E,N=map(int,input().split())
    li=[int(input()) for _ in range(N)]
    print(sum([1 for i in li if i>E]))