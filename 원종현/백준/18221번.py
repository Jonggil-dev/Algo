import sys
input=sys.stdin.readline

N=int(input())
li=[]
a,b=0,0
for i in range(N):
    tmp=list(map(int,input().split()))
    li.append(tmp)
    if 5 in tmp:
        a=(tmp.index(5),i)
    if 2 in tmp:
        b=(tmp.index(2),i)

x1,x2=min(a[0],b[0]),max(a[0],b[0])
y1,y2=min(a[1],b[1]),max(a[1],b[1])
cnt=0
for i in range(y1,y2+1):
    cnt+=li[i][x1:x2+1].count(1)
if cnt>=3 and (x1-x2)**2+(y1-y2)**2>=25:
    print(1)
else:
    print(0)