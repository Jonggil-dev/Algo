import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
li.sort()

if N%2:
    K=(N//2)+1
else:
    K=N//2

res=0
for i in range(K):
    tmp=li[i]
    while tmp>1:
        tmp//=2
        res+=1
print(res+1)