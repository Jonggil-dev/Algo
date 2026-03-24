N=int(input())
A,Pa,B,Pb=map(int,input().split())
a,b=0,0
for x in range(N//Pa+1):
    y=(N-x*Pa)//Pb
    now=x*A+y*A
    if A*a+B*b<=A*x+B*y:
        a,b=x,y
print(a,b)