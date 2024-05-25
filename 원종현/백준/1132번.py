N=int(input())
d=[[0,0] for _ in range(10)]
res=0
for i in range(N):
    S=input()
    d[ord(S[0])-ord('A')][1]=1
    for j in range(len(S)):
        d[ord(S[j])-ord('A')][0]+=10**(len(S)-j-1)
d.sort()
if d[0][1]:
    for i in range(1,10):
        if not d[i][1]:
            del d[i]
            break
res=0
for i in range(1,10):
    res+=(d[-i][0])*(10-i)
print(res)