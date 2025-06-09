import sys
input=sys.stdin.readline
N,K,T=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
A.append(float('inf'))
stk=[]

idx=0
for i in range(K):
    while idx<N and A[idx]<T:
        stk.append(A[idx])
        idx+=1
    if len(stk)==0:
        break
    T+=stk.pop()

print(T)