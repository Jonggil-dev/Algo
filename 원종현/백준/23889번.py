N,M,K=map(int,input().split())
li=list(map(int,input().split()))
s=list(map(lambda x:int(x)-1,input().split()))
s.append(N)

d={}
for i in range(len(s)-1):
    st,end=s[i],s[i+1]
    v=0
    for j in range(st,end):
        v+=li[j]
    d[st]=v
res=sorted(sorted([(k+1,v) for k,v in d.items()],key=lambda x:(-x[1],x[0]))[:M],key=lambda x:x[0])
for i in res:
    print(i[0])