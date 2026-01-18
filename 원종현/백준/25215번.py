S=input()
res=len(S)
chk=0
for i in range(len(S)):
    now=S[i]
    up_now=now.isupper()
    if up_now and not chk:
        chk=0 if i<len(S)-1 and S[i+1].islower() else 1
        res+=1
    elif not up_now and chk:
        res+=1
        chk=1 if i<len(S)-1 and S[i+1].isupper() else 0
print(res)