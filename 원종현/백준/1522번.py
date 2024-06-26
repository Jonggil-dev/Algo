s=input()
x=s.count('a')
s+=s[0:x-1]
res=10**9
for i in range(len(s)-(x-1)):
    res=min(res,s[i:i+x].count('b'))
print(res)