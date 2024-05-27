K,S,N=input().split()
dir={chr(i+65):i+1 for i in range(8)}
reverse_dir={i+1:chr(i+65) for i in range(8)}
K=[9-int(K[1]),dir[K[0]]]
S=[9-int(S[1]),dir[S[0]]]
d={"R":[0,1],"L":[0,-1],"B":[1,0],"T":[-1,0],"RT":[-1,1],"LT":[-1,-1],"RB":[1,1],"LB":[1,-1]}
def func(a,b):
    return [a[0]+b[0],a[1]+b[1]]

for i in range(int(N)):
    s=input()
    nK=func(K,d[s])
    if nK==S:
        nS=func(S,d[s])
        if 1<=nS[0]<=8 and 1<=nS[1]<=8:
            K=nK
            S=nS
    else:
        if 1<=nK[0]<=8 and 1<=nK[1]<=8:
            K=nK

print(reverse_dir[K[1]]+str(9-K[0]))
print(reverse_dir[S[1]]+str(9-S[0]))