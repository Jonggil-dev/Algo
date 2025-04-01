import sys,math
input=sys.stdin.readline
rw='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N=int(input())
d={}
for _ in range(N):
    cnt=0
    S=input().rstrip()
    for i in range(len(S)):
        if S[i].isupper():
            continue
        S=S.replace(S[i],rw[cnt])
        cnt+=1
    if S not in d:
        d[S]=1
    else:
        d[S]+=1

res=0
for i in d.values():
    res+=math.comb(i,2)
print(res)