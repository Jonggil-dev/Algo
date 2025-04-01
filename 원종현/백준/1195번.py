N=input()
M=input()
if len(N)<len(M):
    N,M=M,N
res=len(N)+len(M)
N='0'*len(M)+N
ml=len(M)
for i in range(1,len(N)):
    M='0'+M
    c=1
    for j in range(ml,min(len(M),len(N))):
        if M[j]=='0' or N[j]=='0':
            continue
        if N[j]=='2' and N[j]==M[j]:
            c=0
            break
    if c:
        t=0
        for i in range(max(len(N),len(M))):
            if (i<len(N) and N[i]!='0') or (i<len(M) and M[i]!='0'):
                t+=1
        res=min(res,t)
print(res)