N,S,R=map(int,input().split())

b=set(map(int,input().split()))
o=set(map(int,input().split()))
res=0
tmp=b&o
b=list(b-tmp)
o=list(o-tmp)
b.sort()
for i in b:
    if i-1 in o:
        o.remove(i-1)
    elif i+1 in o:
        o.remove(i+1)
    else:
        res+=1
print(res)