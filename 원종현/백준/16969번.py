s=input()
res=0
if s[0]=='d':
    res=10
if s[0]=='c':
    res=26
for i in range(1,len(s)):
    if s[i]=='d':
        if s[i-1]==s[i]:
            res*=9
        else:
            res*=10
    elif s[i]=='c':
        if s[i-1]==s[i]:
            res*=25
        else:
            res*=26
    res%=1000000009
res%=1000000009
print(res)