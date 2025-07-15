K,C=int(input()),int(input())
res=[]
for i in range(C):
    M,N=map(int,input().split())
    if M<N:
        res.append('0'if N-M-1>=K-N+1 else '1')
    elif M>N:
        res.append('0'if M-N-1>K-M+1 else'1')
    else:
        res.append('1')
print(*res,sep='\n')