A,B=map(int,input().split())
M=int(input())
li=list(map(int,input().split()))[::-1]
res=[]
tmp=0
for i in range(len(li)):
    tmp+=li[i]*(A**i)
while tmp!=0:
    res.append(tmp%B)
    tmp//=B
print(" ".join(map(str,res[::-1])))