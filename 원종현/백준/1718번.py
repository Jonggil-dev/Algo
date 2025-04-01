S=input()
key=input()
key=key*(len(S)//len(key)+1)
t=[97+i for i in range(26)]
res=''
print(S,key,len(S))
for i in range(len(S)):
    print(ord(S[i]),ord(key[i]),chr(97))
    if S[i]==' ':
        res+=' '
    else:
        res+=chr(t[ord(S[i])-ord(key[i])-1])
    print(res)
print(res)