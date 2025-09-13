import sys
input=sys.stdin.readline

N=int(input())
li=[list(map(int,input().split())) for i in range(N)]
x=sorted(li,key=lambda x:x[0])[N//2][0]
y=sorted(li,key=lambda x:x[1])[N//2][1]
res=0
for i in range(N):
    res+=(abs(x-li[i][0])+abs(y-li[i][1]))
print(res)