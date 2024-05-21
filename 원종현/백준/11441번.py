import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
sli=[0]*(N)
sli[0]=li[0]
for i in range(1,N):
    sli[i]=sli[i-1]+li[i]
M=int(input())
for i in range(M):
    a,b=map(int,input().split())
    print(sli[b-1]-(sli[a-2] if a-2>=0 else 0))