d=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A=input()
B=input()
res=''
for i in range(len(A)):
    res+=str(d[ord(A[i])-65])+str(d[ord(B[i])-65])
tmp=''
while len(res)!=2:
    for i in range(1,len(res)):
        tmp+=str((int(res[i])+int(res[i-1])))[-1]
    res=tmp
    tmp=''
print("%2s"%res)