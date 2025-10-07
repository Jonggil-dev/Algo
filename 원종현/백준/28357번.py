import sys
input=sys.stdin.readline

N,K=input().split()
li=set()
for i in range(int(N)):
    li.add(input().rstrip())

P=len(li)
if K=='Y':
    print(P)
elif K=='F':
    print(P//2)
else:
    print(P//3)