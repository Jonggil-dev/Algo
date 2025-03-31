N,M=map(int,input().split())
li=list(map(int,input().split()))
p,m=[i for i in li if i>0],[i for i in li if i<0]
p.sort(reverse=True)
m.sort()
se=[]
i=0
while i<len(p):
    se.append(p[i])
    i+=M
i=0
while i<len(m):
    se.append(abs(m[i]))
    i+=M
se.sort(reverse=True)
res=se[0]+sum([i*2 for i in se[1:]])
print(res)