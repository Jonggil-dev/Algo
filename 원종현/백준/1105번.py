a,b=input().split()
res=0
if len(a)!=len(b):
    print(0)
else:
    for i in range(len(a)):
        if a[i]==b[i]:
            if a[i]=='8':
                res+=1
            else:
                break
    print(res)