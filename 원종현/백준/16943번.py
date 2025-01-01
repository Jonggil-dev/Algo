from itertools import permutations
A,B=input().split()
res=-1
tmp=[]
for i in range(len(A)):
    tmp.append(A[i])
for i in permutations(A,len(A)):
    s=''
    for j in range(len(list(i))):
        s+=i[j]
    if s[0]=='0':
        continue
    t=int(s)
    if t<int(B):
        res=max(res,t)
print(res)