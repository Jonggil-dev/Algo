M,N=map(int,input().split())
d={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
r=[]
for i in range(M,N+1):
    tmp=[d[j] for j in str(i)]
    r.append((' '.join(tmp),i))
r.sort(key=lambda x:x[0])
c=0
for x,y in r:
    print(y,end=" ")
    c+=1
    if c%10==0:
        print()