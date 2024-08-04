import sys
input=sys.stdin.readline

N,M=map(int,input().split())
tmp=1

for _ in range(M):
    i=int(input())
    K=list(map(int,input().split()))
    for j in range(i-1):
        if K[j]<K[j+1]:
            tmp=0
            break
    if not tmp:
        break
print("Yes" if tmp else "No")