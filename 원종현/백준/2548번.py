import sys
input=sys.stdin.readline
N=int(input())
li=sorted(list(map(int,input().split())))
if not N%2:
    print(li[N//2-1])
else:
    print(li[N//2])