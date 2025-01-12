N=int(input())
li=[int(input()) for _ in range(N)]
sli=sorted(li)
res=0
if N==1:
    print(1)
else:
    for i in range(N):
        for j in range(N):
            if li[i]==sli[j]:
                sli[j]=10000
                break
        if j==0 and sli[j+1]!=10000:
            res+=1
        elif j==N-1 and sli[j-1]!=10000:
            res+=1
        elif sli[j-1]==10000 or sli[j+1]==10000:
            continue
        else:
            res+=1
print(res)