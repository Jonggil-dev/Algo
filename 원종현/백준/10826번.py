import sys
input=sys.stdin.readline
N=int(input())
li=[0,1]
for i in range(2,N+1):
    li.append(li[i-1]+li[i-2])
print(li[N])