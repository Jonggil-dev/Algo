N=int(input())
li=[*map(int,input().split())]

r=li[::-1]
tmp=1
a,b=1,1
for i in range(len(r)):
    if not i:
        b=r[i]
        continue
    a=r[i]*b+a
    a,b=b,a
print(b-a,b)