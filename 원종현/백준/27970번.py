S=input()
mod=10**9+7
res=0
p=1
for i in range(len(S)):
    if S[i]=='O':
        res+=p
        res%=mod
    p*=2
    p%=mod
print(res)