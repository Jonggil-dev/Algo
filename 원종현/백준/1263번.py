import sys
input=sys.stdin.readline

N=int(input())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append((b,a))
li.sort(reverse=True)
res=li[0][0]-li[0][1]
for i in range(1,N):
    if res>li[i][0]:
        res=li[i][0]-li[i][1]
    else:
        res-=li[i][1]
print(res if res>=0 else -1)