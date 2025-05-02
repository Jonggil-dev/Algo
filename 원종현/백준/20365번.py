N=int(input())
S=input()
d={"R":0,"B":0}
d[S[0]]=1
for i in range(1,N):
    if S[i]!=S[i-1]:
        d[S[i]]+=1
print(min(d['R'],d['B'])+1)