N=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
res=[]
for i in range(N):
    now=li1[i]
    le,ri=i+1,N-1
    tmp=i
    while le<=ri:
        mid=(le+ri)//2
        if now<li2[mid]:
            ri=mid-1
        else:
            le=mid+1
            tmp=mid
    res.append(str(tmp-i))
print(' '.join(res))