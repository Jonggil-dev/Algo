N=int(input())
x1,y1=map(int,input().split())
res=0
for i in range(N-1):
    x2,y2=map(int,input().split())
    if x1<=y2<=y1:
        continue
    if x1<=x2<=y1 and not x1<=y2<=y1:
        y1=y2
    else:
        res+=abs(y1-x1)
        x1,y1=x2,y2
print(res+abs(y1-x1))