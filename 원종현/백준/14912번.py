N,d=map(int,input().split())
li=[]
r=0
for i in range(1,N+1):
    r+=str(i).count(str(d))
print(r)