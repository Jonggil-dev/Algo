import sys
input=sys.stdin.readline

li=[]
for _ in range(int(input())):
    n,d,m,y=input().rstrip().split()
    d,m,y=map(int,(d,m,y))
    li.append((y,m,d,n))
li.sort()
print(li[-1][3])
print(li[0][3])