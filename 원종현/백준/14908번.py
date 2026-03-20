import sys
input=sys.stdin.readline

N=int(input())
li=[]
for i in range(1,N+1):
    t,s=map(int,input().split())
    li.append((i,t,s))
li.sort(key=lambda x:(x[1]/x[2],x[0]))
print(*[i[0] for i in li])
