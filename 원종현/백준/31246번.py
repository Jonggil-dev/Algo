import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append(b-a)
li.sort()
print(0 if li[K-1]<0 else li[K-1])