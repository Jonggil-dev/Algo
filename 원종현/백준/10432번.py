P=int(input())
for i in range(P):
    t,*tmp=list(map(int,input().split()))
    res=0
    for j in range(1,11):
        for k in range(j,11):
            t=tmp[j:k+1]
            if 0 not in t and min(t)>tmp[j-1] and min(t)>tmp[k+1]:
                res+=1
    print(f"{i+1} {res}")