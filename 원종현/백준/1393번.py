import math

def func(a,b):
    if a<b:
        tmp=a
        a=b
        b=tmp
    while b>0:
        c=b
        b=a%b
        a=c
    return int(a)

x,y=map(int,input().split())
X,Y,dx,dy=map(int,input().split())
B=func(dx,dy)
dx/=B
dy/=B
sx,sy=X,Y

while True:
    dis=math.sqrt(((x-sx)**2)+((y-sy)**2))
    if dis<math.sqrt(((x-X)**2)+((y-Y)**2)):
        print(sx,sy)
        break
    sx,sy=X,Y
    X+=int(dx)
    Y+=int(dy)
