A=input()
B=input()
res=0
if sorted(A)!=sorted(B):
    print(-1)
else:
    now=len(A)-1
    if now==0:
        if A==B:
            print(0)
        else:
            print(-1)
    else:
        for i in range(len(A)-1,-1,-1):
            if A[i]!=B[now]:
                res+=1
            else:
                now-=1
        print(res)