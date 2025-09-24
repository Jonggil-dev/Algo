a,b=input().split()
b=int(b)
idx=(len(a)-1)-a.find('.')
a=a.replace('.','')
res=str(int(a)**b)
idx*=b

if len(res)<idx:
    res='0'*(idx-len(res))+res
res=res[:-idx]+'.'+res[-idx:]
print(res if res[0]!='.' else '0'+res)
