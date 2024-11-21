def func(v):
    tmp=''
    c=12
    while c>=0:
        mod,v=divmod(v,26**c)
        tmp+=chr(mod+97)
        c-=1
    return tmp
T=int(input())
if T==1:
    A,B=map(int,input().split())
    print(func(A+B))
else:
    S=input()
    res=0
    while S:
        res+=(ord(S[-1])-97)*(26**(13-len(S)))
        S=S[:-1]
    print(res)
