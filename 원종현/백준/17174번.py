A,B=map(int,input().split())
r=A
c=A//B
while c//B!=0:
    r+=c
    c=c//B
print(r+c)