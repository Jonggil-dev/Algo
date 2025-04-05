N=int(input())
S=input()
def func(S):
    return ''.join([S[i] for i in range(len(S)) if i%2==0]+[S[i] for i in range(len(S)-1,-1,-1)if i%2])

B=S
if N<1000:
    for i in range(N):
        B=func(B)
    print(B)
else:
    t=0
    for i in range(1000):
        B=func(B)
        if B==S:
            t=i+1
    N%=t
    for i in range(N):
        S=func(S)
    print(S)
