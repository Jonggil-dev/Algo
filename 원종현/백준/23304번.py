import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
print(*sorted(li))