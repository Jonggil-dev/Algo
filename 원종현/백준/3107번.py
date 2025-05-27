li=input().split(":")
if li[0]=='':li=li[1:]
if li[-1]=='':li=li[:-1]
res=''
for i in li:
    if i=='':
        res+='0000:'*(9-len(li))
    else:
        res+=i.zfill(4)+':'
print(res[:-1])
