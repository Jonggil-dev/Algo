import sys
input=sys.stdin.readline
S=input().rstrip()
N=int(input())
res=0
for i in range(N):
    now=input().rstrip()
    if S in now*2:
        res+=1
print(res)