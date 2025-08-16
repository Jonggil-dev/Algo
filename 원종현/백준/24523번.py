N=int(input())
li=list(map(int,input().split()))
res=[]
a,b=0,1
while a<=b:
    if a==N-1:
        break
    if li[a]!=li[b]:
        res+=[b+1]*(b-a)
        a=b
        b+=1
    elif b==N-1 and li[a]==li[b]:
        res+=[-1]*(b-a)
        break
    elif li[a]==li[b]:
        b+=1
res.append(-1)
print(*res)