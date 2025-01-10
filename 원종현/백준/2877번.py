N=int(input())
res=''
while N>0:
    m=N%2
    N//=2
    if m==0:
        N-=1
        res='7'+res
    else:
        res='4'+res
print(res)