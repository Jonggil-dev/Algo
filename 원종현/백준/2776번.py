import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    l1=set(list(map(int,input().split())))
    M=int(input())
    for i in list(map(int,input().split())):
        print(1 if i in l1 else 0)