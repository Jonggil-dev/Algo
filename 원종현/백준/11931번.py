import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
li.sort(reverse=True)
print(*li,sep="\n")