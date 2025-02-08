import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
li.sort()
print(*li,sep='\n')