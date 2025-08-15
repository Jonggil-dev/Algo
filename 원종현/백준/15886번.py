N=int(input())
S=input()
res=0
for i in range(N-1):
    if S[i:i+2]=='EW':res+=1
print(res)