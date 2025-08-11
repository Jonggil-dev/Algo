N=int(input())
li=[i for i in range(1,N+1)]
a,b=0,0
while len(li)>1:
    a+=1
    b+=a**3-1
    b%=len(li)
    li.pop(b)
print(li[0])