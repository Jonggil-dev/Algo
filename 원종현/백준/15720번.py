b,c,d=map(int,input().split())
B=list(map(int,input().split()))
S=list(map(int,input().split()))
E=list(map(int,input().split()))

B.sort(reverse=True)
S.sort(reverse=True)
E.sort(reverse=True)

total=sum(B)+sum(S)+sum(E)
print(total)
for i in range(min(len(B),len(S),len(E))):
    temp=(B[i]+S[i]+E[i])
    total-=temp//10
print(total)