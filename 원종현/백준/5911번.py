N,B=map(int,input().split())
P,S=[],[]
res=0

for i in range(N):
    p,s=map(int,input().split())
    P.append(p)
    S.append(s)
for i in range(N):
    tmp=[]
    for j in range(N):
        tmp.append(S[j]+(P[j]//2 if i==j else P[j]))
    tmp.sort()
    tot=0
    cnt=0
    for j in range(N):
        tot+=tmp[j]
        if tot>B:
            break
        cnt+=1
    res=max(res,cnt)
print(res)