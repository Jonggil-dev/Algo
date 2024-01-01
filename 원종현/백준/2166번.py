import sys
input = sys.stdin.readline

li=[]
N=int(input())
for _ in range(N):
    x,y=map(int,input().split())
    li.append([x,y])
li.append(li[0])
a,b=0,0
for i in range(N):
    a+=li[i][0]*li[i+1][1]
    b+=li[i][1]*li[i+1][0]    
print(round(abs(a-b)/2,1))
