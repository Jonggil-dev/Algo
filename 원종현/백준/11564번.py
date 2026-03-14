K,A,B=map(int,input().split())
res=0
if A*B<0:
    res=1
    A,B=abs(A),abs(B)
    res+=(A//K+B//K)
else:
    A,B=min(abs(A),abs(B)),max(abs(A),abs(B))
    res+=((B//K)-((A+K)//K)+1)
    if A%K==0:
        res+=1
print(res)