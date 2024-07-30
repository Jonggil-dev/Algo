N=int(input())
so=[1]*(102**2)
se=set()
for i in range(2,102**2):
    if so[i]:
        se.add(i)
        for i in range(i,102**2,i):
            so[i]=0
se=sorted(list(se))
for i in range(len(se)):
    tmp=se[i]*se[i+1]
    if N<tmp:
        print(tmp)
        break
