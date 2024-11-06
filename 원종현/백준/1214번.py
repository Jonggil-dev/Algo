D,P,Q=map(int,input().split())
if P<Q:
    P,Q=Q,P
res=(D+P-1)//P*P
for i in range(0,min(P*Q,D+1),P):
    tmp=i+(D-i+Q-1)//Q*Q
    res=min(tmp,res)
print(res)