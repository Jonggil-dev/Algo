import sys
input=sys.stdin.readline
N=int(input())
li=sorted([int(input()) for _ in range(N)])
r=1
for i in li:
    c=1
    for j in range(i+1,i+5):
        if j in li:
            c+=1
    r=max(r,c)
print(0 if r>=5 else 5-r)