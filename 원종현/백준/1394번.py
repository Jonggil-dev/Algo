S=input()
code=input()
c=len(code)
res=0
d={}
for i in range(len(S)):
    if S[i] not in d:
        d[S[i]]=i

for i in code:
    idx=d[i]
    res+=idx+1
    if c>1:
        res*=len(S)
        res%=900528
    c-=1
print(res%900528)