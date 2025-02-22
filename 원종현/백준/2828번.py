import sys
input=sys.stdin.readline

N,M=map(int,input().split())
J=int(input())
now=1
li=[]
res=0
for i in range(J):
    li.append(int(input()))
for i in li:
    if now<=i and now+(M-1)>=i:
        continue
    elif now>i:
        res+=abs(i-now)
        now=i
    else:
        res+=i-(M-1)-now
        now=i-(M-1)
print(res)