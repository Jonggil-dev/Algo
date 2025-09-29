import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append((i+1,a,b))
li.sort(key=lambda x:(1-x[2])/x[1])
for i in li:
    print(str(i[0]))