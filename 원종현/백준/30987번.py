import sys
input=sys.stdin.readline

def func(a,b,c,d,e,f):
    return ((a*(f**3))//3)+((b*f**2)//2)+(c*f)-(((d*f**2)//2)+e*f)

x1,x2=map(int,input().split())
a,b,c,d,e=map(int,input().split())

print(func(a,b,c,d,e,x2)-func(a,b,c,d,e,x1))
