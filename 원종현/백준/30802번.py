import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
T,P=map(int,input().split())
r1,r2,r3=0,0,0
for i in li:
    r1+=i//T+1 if i%T else i//T
print(r1)
print(N//P,N%P)