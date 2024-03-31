import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    li.append(float(input()))
li.sort()
for i in range(7):
    print(f"{li[i]:.3f}")