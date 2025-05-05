N=int(input())
S=list(input())
res=0
for _ in range(N-1):
    s=S[:]
    word=input()
    cnt=0
    for i in word:
        if i in s:
            s.remove(i)
        else:
            cnt+=1
    if cnt<2 and len(s)<2:
        res+=1
print(res)