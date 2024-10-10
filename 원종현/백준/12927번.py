N=list(input())
N.insert(0,'N')
res=0
for i in range(1,len(N)):
    if N[i]=='Y':
        for j in range(i,len(N),i):
            if N[j]=='Y':
                N[j]='N'
            else:
                N[j]='Y'
        res+=1
print(res)