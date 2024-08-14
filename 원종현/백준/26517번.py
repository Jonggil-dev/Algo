K=int(input())
a,b,c,d=map(int,input().split())
if a*K+b==c*K+d:
    print("Yes",a*K+b)
else:
    print("No")