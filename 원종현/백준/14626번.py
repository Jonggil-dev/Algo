S=input()
cnt=sum([int(S[i])*([1,3][i%2]) for i in range(len(S)) if S[i]!='*'])
f=[1,3][S.index('*')%2]
for i in range(10):
    if (cnt+i*f)%10==0:
        print(i)
        break
