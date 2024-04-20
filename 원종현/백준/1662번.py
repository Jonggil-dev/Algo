S=input()
li=S.split()

q=[]
res=0
before=0
for i in S:
    if i=="(":
        q.append([res-1,before])
        res=0
    elif i==")":
        tmp=q.pop()
        res=res*tmp[1]+tmp[0]
    else:
        res+=1
        before=int(i)
print(res)