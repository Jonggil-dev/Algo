import sys
input=sys.stdin.readline
INF=1000000007
N=int(input())
li=list(map(int,input().split()))
res=0
tmp=0
for i in li:
    tmp=((tmp+1)*i)%INF
    res=(res+tmp)%INF
print(res)