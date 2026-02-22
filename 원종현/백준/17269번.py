d={'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}
N,M=map(int,input().split())
A,B=input().split()

li=[]
for i in range(min(N,M)):
    li+=A[i]+B[i]

if N>M:
    li+=A[min(N,M):]
else:
    li+=B[min(N,M):]

res=[]
for i in li:
    res.append(d[i])

while len(res)>2:
    tmp=[]
    for i in range(1,len(res)):
        now=res[i-1]+res[i]
        if now>=10:
            now-=10
        tmp.append(now)
    res=tmp
print(f'{res[0]*10+res[1]}%')